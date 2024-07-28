from cs50 import get_string


def luhn_check(card_number):
    total = 0
    reverse_digits = card_number[::-1]

    # Apply Luhn's Algorithm
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0


def card_type(card_number):
    if luhn_check(card_number):
        if card_number.startswith('34') or card_number.startswith('37'):
            if len(card_number) == 15:
                return "AMEX"
        elif card_number.startswith('4'):
            if len(card_number) in [13, 16]:
                return "VISA"
        elif 51 <= int(card_number[:2]) <= 55:
            if len(card_number) == 16:
                return "MASTERCARD"

    return "INVALID"


def main():
    card_number = get_string("Number: ")
    result = card_type(card_number)
    print(result)


if __name__ == "__main__":
    main()
