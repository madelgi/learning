#include <stdio.h>
#include <stdlib.h>

double convert_age(int years)
{
    double cf = 3.156e7;
    return (cf * years);
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Hey, pass an integer as argument.\n");
        return 1;
    }
    int years = atoi(argv[1]);
    printf("Your age in seconds is %f.\n", convert_age(years));
    return 0;
}
