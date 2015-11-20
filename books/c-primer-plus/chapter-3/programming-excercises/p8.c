/* Write a program that requests a volume in cups and
 * that displays the equivalent volumes in pints, ounces
 * tablespoons, and teaspoons
 */
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: %s <INTEGER>.\n", argv[0]);
        return 1;
    }

    int vol = atoi(argv[1]);
    printf("The volume in pints: %.3f.\n", (float)vol/2.0);
    printf("The volume in ounces: %d.\n", vol*8);
    printf("The volume in tablespoons: %d.\n", vol*16);
    printf("The volume in teaspoons: %d.\n", vol*48);
    return 0;
}
