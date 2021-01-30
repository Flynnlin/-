#include<stdio.h>
int main(){
    int a=10,b=20,s,t,*pa,*pb;
    pa=&a;
    pb=&b;
    s=*pa+*pb;
    t=*pa**pb;
    printf("a=%d\nb=%d,a+b=%d,a*b=%d",*pa,*pb,s,t);
}