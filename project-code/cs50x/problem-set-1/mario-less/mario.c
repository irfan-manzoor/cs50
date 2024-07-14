#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Prompt the user for a valid height
    do
    {
        height = get_int("Enter the height of the pyramid: ");
    }
    while (height <= 0);

    // Print the pyramid
    for (int i = 1; i <= height; i++)
    {
        // Print spaces
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }
        // Print hashes
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
