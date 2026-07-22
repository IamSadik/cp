#include <stdio.h>

void test(int *p)
{
    p = NULL;
}

int main()
{
    int a = 10;
    int *ptr = &a;

    test(ptr);

    printf("%d", *ptr);
}
