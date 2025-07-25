def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # accept a str as input, remove the leading $,
    # return the amount as a float.
    bill = float(d.removeprefix("$"))
    return (bill)

def percent_to_float(p):
    # accept a str as input, remove the trailing %,
    # return the percentage as a float
    percentage = float(p.removesuffix("%"))
    tip = percentage / 100
    return (tip)

main()
