#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
int compute_score(char word[]);

int main(void)
{
    char word1[50], word2[50];

    // Prompt for input from Player 1
    printf("Player 1: ");
    scanf("%s", word1);

    // Prompt for input from Player 2
    printf("Player 2: ");
    scanf("%s", word2);

    // Compute the scores
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Determine the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}

// Function to compute the Scrabble score for a given word
int compute_score(char word[])
{
    // Points for each letter in Scrabble
    int points[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                      1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    int score = 0;
    int len = strlen(word);

    for (int i = 0; i < len; i++)
    {
        if (isalpha(word[i]))
        {
            // Convert letter to upper case and compute score
            score += points[toupper(word[i]) - 'A'];
        }
    }

    return score;
}
