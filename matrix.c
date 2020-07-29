#include <stdio.h>

int main()
{
   int A[1][1];
   int a, b, c, d;
   scanf("%d", &a);
   scanf("%d", &b);
   scanf("%d", &c);
   scanf("%d", &d);
   A[0][0] = 1;
   A[0][1] = 2;
   A[1][0] = 3;
   A[1][1] = 4;
   printf("%d %d\n", a, b);
   printf("%d %d\n", c, d);
}
