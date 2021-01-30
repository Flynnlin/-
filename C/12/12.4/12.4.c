#include<stdio.h>
int main(){
    unsigned a,b;
    printf("input a number");
    scanf("%d",&a);
    b=a>>5;
    printf("a=%d\ta>>5=%d\n",a,b);
}