def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0 or x > y:
            raise ValueError
        percentage = (x / y) * 100
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f"{round(percentage)}%"
    except (ValueError, ZeroDivisionError):
        return None

def main():
    while True:
        fraction = input("Enter the fuel fraction (in the format X/Y): ")
        percentage = calculate_fuel_percentage(fraction)
        if percentage is not None:
            print(percentage)
            break
        else:
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()
