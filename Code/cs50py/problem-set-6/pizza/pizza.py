import csv
import sys
from tabulate import tabulate

def read_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [dict(row) for row in reader]
        return data
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    # Validate command-line arguments
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Usage: python pizza.py <file.csv>")

    # Read data from CSV file
    pizza_data = read_csv(sys.argv[1])

    # Format data into a table
    headers = list(pizza_data[0].keys())
    table_data = [[row[header] for header in headers] for row in pizza_data]
    table = [headers] + table_data

    # Print the table using tabulate
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
