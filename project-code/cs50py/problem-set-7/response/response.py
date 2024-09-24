import validators

def validate_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    email = input("Please enter an email address: ")
    result = validate_email(email)
    print(result)
