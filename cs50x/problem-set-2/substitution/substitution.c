#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes
int is_valid_key(char *key);
void encrypt(char *plaintext, char *key);

int main(int argc, char *argv[])
{
    // Check for correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Check if the key is valid
    char *key = argv[1];
    if (!is_valid_key(key))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }

    // Prompt user for plaintext
    char plaintext[1000];
    printf("plaintext:  ");
    fgets(plaintext, sizeof(plaintext), stdin);

    // Encrypt the plaintext
    printf("ciphertext: ");
    encrypt(plaintext, key);

    return 0;
}

// Function to check if the key is valid
int is_valid_key(char *key)
{
    if (strlen(key) != 26)
    {
        return 0;
    }

    int counts[26] = {0};
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return 0;
        }

        int index = toupper(key[i]) - 'A';
        if (counts[index] > 0)
        {
            return 0;
        }
        counts[index]++;
    }

    return 1;
}

// Function to encrypt the plaintext using the substitution cipher
void encrypt(char *plaintext, char *key)
{
    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        char c = plaintext[i];

        if (isalpha(c))
        {
            char base = islower(c) ? 'a' : 'A';
            int index = toupper(c) - 'A';
            char substitution = islower(c) ? tolower(key[index]) : toupper(key[index]);
            printf("%c", substitution);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}
