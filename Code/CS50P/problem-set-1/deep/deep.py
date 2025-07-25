# user input

answer = input("What is the answer to the Great Question of Life, the Universe and Everything: ")

# output "Yes" if the answer is "42" or "forty-two" or "forty two"

if answer.strip() == "42" or answer.strip().lower() == "forty-two" or answer.strip().lower() == "forty two":
    print("Yes")
else:
    print("No")
