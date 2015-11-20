#include <stdlib.h>
#include <stdio.h>

void print_reverse(int *arr, size_t count)
{
    for (int i=count-1; i >= 0; i--) {
        printf("%d\n", arr[i]);
    }
}

int main(int argc, char* argv[])
{
    if (argc != 2) {
        printf("yuh don messed up.\n");
        return -1;
    }
    int n = atoi(argv[1]);
    int arr[n];
    int val;
    printf("Start entering numbers.\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &val);
        arr[i] = val;
    }
    print_reverse(arr, sizeof(arr)/sizeof(*arr));
}
