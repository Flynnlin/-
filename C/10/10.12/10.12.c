#include<stdio.h>
int main(){
    int a[10],i,*p=a;
    for(i=0;i<10;){
        *p=i;
        printf("a[%d]=%d\n",i++,*p++);
    }
}