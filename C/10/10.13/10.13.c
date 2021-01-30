#include<stdio.h>
//错误示范 10.14改正
int main(){
    int *p,i,a[10];
    p=a;
    for(i=0;i<10;i++){
        *p++=i;
    }
    //错误，这里p已经自加了，后面输出还在自加
    for(i=0;i<10;i++){
        printf("a[%d]=%d\n",i,*p++);
    }
}