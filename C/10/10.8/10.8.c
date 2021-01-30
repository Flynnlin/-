#include<stdio.h>
int main(){
    int a,b,c,*pmax,*pmin;
    printf("input 3 number");
    scanf("%d%d%d",&a,&b,&c);
    if(a>b){
        pmax=&a;
        pmin=&b;
    }else{
        pmax=&b;
        pmin=&a;
    }
    if(c>*pmax){
        pmax=&c;
    }else{
        pmin=&c;
    }
    printf("max=%d,min=%d",*pmax,*pmin);
}