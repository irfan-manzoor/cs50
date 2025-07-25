def main():
    grocery_dict = {}
    # print("Enter your grocery items (press Ctrl+D to end):")
    try:
        while True:
            item = input().strip().lower()
            grocery_dict[item] = grocery_dict.get(item, 0) + 1
    except EOFError:
        pass

    # print("\nYour grocery list:")
    for item, count in sorted(grocery_dict.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
