#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
void encrypt(char *plaintext, int key);

int main(int argc, char *argv[])
{
    // Check for correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if the argument is a non-negative integer
    for (int i = 0; argv[1][i] != '\0'; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert the key from string to integer
    int key = atoi(argv[1]);

    // Prompt user for plaintext
    char plaintext[1000];
    printf("plaintext:  ");
    fgets(plaintext, sizeof(plaintext), stdin);

    // Remove the newline character from fgets
    size_t len = strlen(plaintext);
    if (len > 0 && plaintext[len - 1] == '\n')
    {
        plaintext[len - 1] = '\0';
    }

    // Encrypt the plaintext
    printf("ciphertext: ");
    encrypt(plaintext, key);

    return 0;
}

// Function to encrypt the plaintext using the Caesar cipher
void encrypt(char *plaintext, int key)
{
    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        char c = plaintext[i];

        if (isalpha(c))
        {
            char base = islower(c) ? 'a' : 'A';
            printf("%c", (c - base + key) % 26 + base);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}
