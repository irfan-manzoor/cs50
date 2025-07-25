def get_fruit_calories(fruit):
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "kiwifruit": 90,
        "pear": 100,
        "sweet cherries": 100
    }
    return fruit_calories.get(fruit.lower(), None)

def main():
    fruit = input("Enter a fruit: ").lower()
    calories = get_fruit_calories(fruit)
    if calories is not None:
        print(f"There are {calories} calories in one portion of {fruit.capitalize()}.")
    else:
        print("")

if __name__ == "__main__":
    main()
