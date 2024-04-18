import inflect

def bid_adieu(names):
    p = inflect.engine()
    count = len(names)

    if count == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif count == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = ", ".join(names[:-1])
        farewell += f", and {names[-1]}"
        return f"Adieu, adieu, to {farewell}"

def main():
    names = []
    try:
        while True:
            name = input("Enter a name: ")
            names.append(name)
    except EOFError:
        pass

    print(bid_adieu(names))

if __name__ == "__main__":
    main()
