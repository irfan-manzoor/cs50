from cs50 import get_float


def main():
    while True:
        change_owed = get_float("Change owed: ")
        if change_owed >= 0:
            break

    # Convert dollars to cents to avoid floating-point precision issues
    cents = round(change_owed * 100)

    coins = 0

    # Calculate the number of quarters
    coins += cents // 25
    cents %= 25

    # Calculate the number of dimes
    coins += cents // 10
    cents %= 10

    # Calculate the number of nickels
    coins += cents // 5
    cents %= 5

    # Calculate the number of pennies
    coins += cents

    print(coins)


if __name__ == "__main__":
    main()
