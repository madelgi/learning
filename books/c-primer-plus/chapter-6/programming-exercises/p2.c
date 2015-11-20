/*
 */
#include <stdio.h>

void repeat_print(char c, int n)
{
    for (int i=0; i<n; i++) {
        printf("%c", c);
    }
    printf("\n");
}

void money_pyramid(int n)
{
    for (int i=1; i<=n; i++) {
        repeat_print('$', i);
    }
}

int main()
{
    printf("How many levels?\n");
    int n;
    scanf("%d", &n);
    money_pyramid(n);
    return 0;
}
