#include <stdio.h>
#include <stdlib.h>

void jolly(int n)
{
    char line[] = "For he's a jolly good fellow!";
    for (int i=0; i<n; i++) {
        printf("%s\n", line);
    }
}

int main(int argc, char *argv[])
{
    int m;
    if (argc != 2) {
        printf("Usage: %s m\n", argv[0]);
    }
    m = atoi(argv[1]);
    jolly(m);
    printf("Which nobody can deny!");
}
