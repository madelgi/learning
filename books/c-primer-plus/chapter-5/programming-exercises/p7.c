/*
 * Requests a type double and prints the value of the number cubed.
 */
#include <stdio.h>

double cube(double n)
{
    return n*n*n;
}

int main(int argc, char* argv[])
{
    printf("Enter a number.\n");
    double n;
    scanf("%lf", &n);
    printf("The cube of %.2f is %.2f.\n", n, cube(n));
}
