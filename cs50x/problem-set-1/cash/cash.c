#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;

    // Prompt the user for the amount of change owed, re-prompt if input is invalid
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Initialize coin counters and available denominations
    int coins = 0;
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;
    int pennies = 1;

    // Calculate the minimum number of coins
    while (cents >= quarters)
    {
        cents -= quarters;
        coins++;
    }
    while (cents >= dimes)
    {
        cents -= dimes;
        coins++;
    }
    while (cents >= nickels)
    {
        cents -= nickels;
        coins++;
    }
    while (cents >= pennies)
    {
        cents -= pennies;
        coins++;
    }

    // Print the total number of coins
    printf("%d\n", coins);

    return 0;
}
