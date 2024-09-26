import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_operands(level)
        correct_answer = x + y
        user_answer = prompt_user(x, y)
        if user_answer == correct_answer:
            score += 1
    print("Your score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_operands(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def prompt_user(x, y):
    attempts = 0
    correct_answer = x + y
    while attempts < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == correct_answer:
                return answer
            else:
                print("EEE")
                attempts += 1
        except ValueError:
            print("EEE")
            attempts += 1
    print(f"The correct answer is {correct_answer}.")
    return None

if __name__ == "__main__":
    main()
