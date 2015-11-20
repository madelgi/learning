#include <stdlib.h>
#include <stdio.h>

int main()
{
    int count = 0;
    char ch;
    while ((ch = getchar()) != '#') {
        count += 1;
    }
}
