from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    try:
        dob = input("Date of Birth: ")
        difference = calculate_age_in_days(dob)
        print(convert(difference))
    except ValueError:
        sys.exit("Invalid date format. Please enter date in YYYY-MM-DD format.")


def calculate_age_in_days(dob):
    try:
        birth_date = date.fromisoformat(dob)
        today = date.today()
        return (today - birth_date).days
    except ValueError:
        raise ValueError("Invalid date format")


def convert(time):
    minutes = time * 24 * 60
    return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"


if __name__ == "__main__":
    main()
