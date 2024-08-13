from cs50 import get_string
import math


def calculate_coleman_liau_index(text):
    # Initialize counts
    letters = 0
    words = 1  # Starting at 1 for the first word
    sentences = 0

    # Count letters, words, and sentences
    for char in text:
        if char.isalpha():
            letters += 1
        elif char in [' ', '\n', '\t']:
            words += 1
        elif char in ['.', '!', '?']:
            sentences += 1

    # Compute averages
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # Calculate Coleman-Liau index
    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)


def main():
    text = get_string("Text: ")

    # Calculate grade level
    grade = calculate_coleman_liau_index(text)

    # Output result
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
