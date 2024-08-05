from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('birthdays.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_upcoming_birthday(month, day):
    today = datetime.today()
    if (today.month == month and today.day < day) or (today.month < month):
        return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        month = int(request.form['month'])
        day = int(request.form['day'])
        notes = request.form.get('notes', '')

        if month < 1 or month > 12 or day < 1 or day > 31:
            error = "Invalid date. Please enter a valid month and day."
        else:
            conn = get_db_connection()
            existing_birthday = conn.execute('SELECT * FROM birthdays WHERE name = ?', (name,)).fetchone()
            if existing_birthday:
                error = "Birthday already exists for this person."
            else:
                conn.execute('INSERT INTO birthdays (name, month, day, notes) VALUES (?, ?, ?, ?)', (name, month, day, notes))
                conn.commit()
            conn.close()

        if error:
            return redirect('/?error=' + error)
        else:
            return redirect('/')
    else:
        conn = get_db_connection()
        search_query = request.args.get('search', '')
        sort_by = request.args.get('sort', 'name')

        if search_query:
            birthdays = conn.execute('SELECT * FROM birthdays WHERE name LIKE ?', ('%' + search_query + '%',)).fetchall()
        else:
            if sort_by == 'date':
                birthdays = conn.execute('SELECT * FROM birthdays ORDER BY month, day').fetchall()
            else:
                birthdays = conn.execute('SELECT * FROM birthdays ORDER BY name').fetchall()

        birthdays = [{
            **dict(birthday),
            'upcoming': get_upcoming_birthday(birthday['month'], birthday['day'])
        } for birthday in birthdays]

        conn.close()

        return render_template('index.html', birthdays=birthdays, edit_id=None, search_query=search_query, sort_by=sort_by, error=request.args.get('error'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM birthdays WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    conn = get_db_connection()
    birthday = conn.execute('SELECT * FROM birthdays WHERE id = ?', (id,)).fetchone()
    conn.close()

    conn = get_db_connection()
    birthdays = conn.execute('SELECT * FROM birthdays').fetchall()
    conn.close()

    return render_template('index.html', birthdays=birthdays, edit_id=id, edit_birthday=birthday, search_query='', sort_by='name', error=None)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name']
    month = int(request.form['month'])
    day = int(request.form['day'])
    notes = request.form.get('notes', '')

    conn = get_db_connection()
    conn.execute('UPDATE birthdays SET name = ?, month = ?, day = ?, notes = ? WHERE id = ?', (name, month, day, notes, id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
