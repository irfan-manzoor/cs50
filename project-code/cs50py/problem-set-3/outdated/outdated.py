import datetime

def get_valid_date():
    months = [
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ]

    while True:
        user_input = input("Please enter a date (in month-day-year format): ").strip()

        try:
            # Try parsing the date input with various formats
            date_obj = None
            for fmt in ["%m/%d/%Y", "%B %d, %Y"]:
                try:
                    date_obj = datetime.datetime.strptime(user_input, fmt)
                    break
                except ValueError:
                    pass

            if date_obj:
                return date_obj.strftime("%Y-%m-%d")
            else:
                print("Invalid date format. Please try again.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    formatted_date = get_valid_date()
    print(formatted_date)
