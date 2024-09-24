#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
int count_letters(char *text);
int count_words(char *text);
int count_sentences(char *text);
int calculate_grade_level(int letters, int words, int sentences);

int main(void)
{
    char text[1000];

    // Prompt user for input
    printf("Text: ");
    fgets(text, sizeof(text), stdin);

    // Calculate the number of letters, words, and sentences
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Calculate the grade level
    int grade = calculate_grade_level(letters, words, sentences);

    // Print the grade level
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }

    return 0;
}

int count_letters(char *text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(char *text)
{
    int count = 0;
    int in_word = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isspace(text[i]))
        {
            if (in_word)
            {
                count++;
                in_word = 0;
            }
        }
        else
        {
            in_word = 1;
        }
    }
    if (in_word)
    {
        count++;
    }
    return count;
}

int count_sentences(char *text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}

int calculate_grade_level(int letters, int words, int sentences)
{
    float L = (float) letters / words * 100;
    float S = (float) sentences / words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    return round(index);
}
