#include<math.h>
#include<stdio.h>
main()
{
    double x,s;
    printf("please type a number\n>");
    scanf("%lf",&x);
    s=sin(x);
    printf("sin of %lf is %lf\n",x,s);
    return;
}
