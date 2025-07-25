import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])


def clean(input_file, output_file):
    try:
        with open(input_file) as input_file:
            reader = csv.DictReader(input_file)
            with open(output_file, "w") as output_file:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
