// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int HASH_TABLE_SIZE = 65536; // A large prime number for better distribution

// Hash table
node *hash_table[HASH_TABLE_SIZE];

// Converts a word to lowercase
void to_lowercase(char *str)
{
    for (int i = 0; str[i]; i++)
    {
        str[i] = tolower(str[i]);
    }
}

// Hashes a word to a number
unsigned int hash_word(const char *word)
{
    unsigned long hash_value = 0;
    while (*word)
    {
        hash_value = (hash_value * 31) + tolower(*word++);
    }
    return hash_value % HASH_TABLE_SIZE;
}

// Returns true if the word is in the dictionary, else false
bool check(const char *word)
{
    char lowercase_word[LENGTH + 1];
    strncpy(lowercase_word, word, LENGTH);
    lowercase_word[LENGTH] = '\0'; // Ensure null termination
    to_lowercase(lowercase_word);

    unsigned int index = hash_word(lowercase_word);
    node *cursor = hash_table[index];
    while (cursor != NULL)
    {
        if (strcmp(cursor->word, lowercase_word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Loads the dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (!file)
    {
        return false;
    }

    char word[LENGTH + 1];
    while (fscanf(file, "%s", word) != EOF)
    {
        node *new_node = malloc(sizeof(node));
        if (!new_node)
        {
            fclose(file);
            return false;
        }
        strcpy(new_node->word, word);

        unsigned int index = hash_word(word);
        new_node->next = hash_table[index];
        hash_table[index] = new_node;
    }

    fclose(file);
    return true;
}

// Returns the number of words in the dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int word_count = 0;
    for (unsigned int i = 0; i < HASH_TABLE_SIZE; i++)
    {
        node *cursor = hash_table[i];
        while (cursor != NULL)
        {
            word_count++;
            cursor = cursor->next;
        }
    }
    return word_count;
}

// Unloads the dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (unsigned int i = 0; i < HASH_TABLE_SIZE; i++)
    {
        node *cursor = hash_table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
