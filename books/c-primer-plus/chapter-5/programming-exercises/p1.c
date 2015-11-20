/* Program that converts time in minutes to time in hours and minutes.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define HOUR 60

int main(int argc, char* argv[])
{
    while (true) {
        printf("Enter a time in minutes.\n");
        int mins;
        scanf("%d", &mins);
        if (mins < 0) {
            break;
        }
        int rem = mins % HOUR;
        int hours = mins/HOUR;
        if (hours == 0) {
            printf("That's %d minutes.\n", mins);
        } else {
            printf("That's equivalent to %d hours and %d minutes.\n", hours, rem);
        }
    }
}
