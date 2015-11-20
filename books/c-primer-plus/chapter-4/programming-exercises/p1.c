#include <stdio.h>

void first_last(char* first, char* last)
{
    printf("\nYour name is: %s, %s\n", last, first);
}

int main(int argc, char* argv[])
{
    // Catch wrong # of arguments
    if (argc != 1) {
        printf("Usage: %s\n.", argv[0]);
        return 1;
    }

    char first[40];
    char last[40];

    printf("Enter your first name.\n");
    scanf("%s", first);
    printf("Enter your last name.\n");
    scanf("%s", last);
    first_last(first, last);
    return 0;
}
