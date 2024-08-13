menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def calculate_total(order):
    total = sum(menu[item] for item in order)
    return total

def main():
    order = []
    try:
        while True:
            item = input("Enter item: ").title()
            if item in menu:
                order.append(item)
                total = calculate_total(order)
                print(f"${total:.2f}")
            else:
                print("Invalid item.")
    except EOFError:
        pass

if __name__ == "__main__":
    main()
