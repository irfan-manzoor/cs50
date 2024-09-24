def main():
    # Prompting the user for input
    user_input = input("Enter a text: ")
    # Calling the shorten function to remove vowels
    shortened_text = shorten(user_input)
    # Outputting the text without vowels
    print("Text without vowels:", shortened_text)


def shorten(word):
    vowels = "AEIOUaeiou"
    output = ""
    for char in word:
        if char not in vowels:
            output += char
    return output


if __name__ == "__main__":
    main()
