# Prompting the user for input
user_input = input("Enter a text: ")

# Removing vowels from the input text
vowels = "AEIOUaeiou"
output = ""
for char in user_input:
    if char not in vowels:
        output += char

# Outputting the text without vowels
print("Text without vowels:", output)
