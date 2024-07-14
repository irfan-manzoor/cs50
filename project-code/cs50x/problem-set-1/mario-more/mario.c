#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // Prompt the user for a valid height between 1 and 8
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Print the pyramid
    for (int i = 1; i <= height; i++)
    {
        // Print spaces for left pyramid
        for (int j = 0; j < height - i; j++)
        {
            printf(" ");
        }
        // Print hashes for left pyramid
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        // Print gap between pyramids
        printf("  ");
        // Print hashes for right pyramid
        for (int k = 0; k < i; k++)
        {
            printf("#");
        }
        // Move to the next line
        printf("\n");
    }
    return 0;
}
