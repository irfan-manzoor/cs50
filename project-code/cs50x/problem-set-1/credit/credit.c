#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
bool check_luhn(long number);
string get_card_type(long number);

int main(void)
{
    long card_number;

    // Prompt the user for the credit card number
    card_number = get_long("Number: ");

    // Validate the card number using the Luhn algorithm and determine the card type
    if (check_luhn(card_number))
    {
        string card_type = get_card_type(card_number);
        printf("%s\n", card_type);
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}

// Function to check if a card number is valid using the Luhn algorithm
bool check_luhn(long number)
{
    int sum = 0;
    bool alternate = false;

    while (number > 0)
    {
        int digit = number % 10;
        number /= 10;

        if (alternate)
        {
            digit *= 2;
            if (digit > 9)
            {
                digit -= 9;
            }
        }

        sum += digit;
        alternate = !alternate;
    }

    return (sum % 10) == 0;
}

// Function to determine the type of card based on the number
string get_card_type(long number)
{
    int length = 0;
    long temp = number;

    while (temp > 0)
    {
        temp /= 10;
        length++;
    }

    long start_digits = number;
    while (start_digits >= 100)
    {
        start_digits /= 10;
    }

    if (length == 15 && (start_digits == 34 || start_digits == 37))
    {
        return "AMEX";
    }
    else if (length == 16 && (start_digits >= 51 && start_digits <= 55))
    {
        return "MASTERCARD";
    }
    else if ((length == 13 || length == 16) && (start_digits / 10 == 4))
    {
        return "VISA";
    }
    else
    {
        return "INVALID";
    }
}
