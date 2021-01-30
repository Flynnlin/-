#include<stdio.h>
int main(){
    char a='a',b='b';
    int p,c,d;
    p=a;
    p=(p<<8)|b;
    d=p&0xff;
    printf("a=%d\nb=%d",p,d);
}