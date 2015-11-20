#include <stdio.h>
#include <string.h>

void first_last(char* first, char* last)
{
    int l_first = strlen(first);
    int l_last = strlen(last);
    printf("%s %s\n", last, first);
    printf("%*d %*d\n", l_last, l_last, l_first, l_first);
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
