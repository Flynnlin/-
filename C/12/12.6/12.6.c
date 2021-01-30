#include<stdio.h>
int main(){
    struct bs{
        unsigned a:1;
        unsigned b:2;
        unsigned c:3;
    }bit,*pbit;
    bit.a=1;
    bit.b=7;
    bit.c=15;
    printf("%d,%d,%d",bit.a,bit.b,bit.c);
}