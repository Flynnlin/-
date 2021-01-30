#include<stdio.h>
int main(){
    int *p1,*p2,*p,a,b;
    printf("please 2 number]\n");
    scanf("%d%d",&a,&b);
    p1=&a;
    p2=&b;
    if(a<b){
        p=p1;
        p1=p2;
        p2=p;
    }
    printf("%d  %d\n",a,b);
    printf("%d   %d",*p1,*p2);
}