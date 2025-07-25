# fuel.py

def convert(fraction):
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
            return round(percentage)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"

def main():
    while True:
        fraction = input("Enter the fuel fraction (in the format X/Y): ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError:
            print("Invalid input. X must be less than or equal to Y.")
        except ZeroDivisionError:
            print("Invalid input. Y cannot be zero.")

if __name__ == "__main__":
    main()
