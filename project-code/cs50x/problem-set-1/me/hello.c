#include <stdio.h>

int main()
{
    char name[50];

    printf("Enter your name: ");
    scanf("%49s", name); // %49s limits input to 49 characters to prevent buffer overflow

    printf("hello, %s\n", name);
    return 0;
}
