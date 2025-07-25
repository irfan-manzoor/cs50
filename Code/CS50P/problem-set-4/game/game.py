import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")

def play_game(level):
    target_number = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                print("Please enter a positive integer.")
            elif guess < target_number:
                print("Too small!")
            elif guess > target_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a positive integer.")

def main():
    level = get_level()
    play_game(level)

if __name__ == "__main__":
    main()
