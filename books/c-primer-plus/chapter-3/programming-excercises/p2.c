#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: %s <INTEGER>.\n", argv[0]);
        return 1;
    }
    int n = atoi(argv[1]);
    if ( !(n > 0 && n < 256) ) {
        printf("%d is invalid. Argument must be between 0 and 255.\n", n);
        return 1;
    }
    printf("The associated char for ASCII %d is %c.\n", n, n);
    return 0;
}
