#include<stdio.h>
int max,min;
void max_min_value(int *array,int n){
    int *p,*array_end;
    array_end=array+n;
    max=min=*array;
    for(p=array+1;p<array_end;p++){
        if(*p>max){
            max=*p;
        }else{
            min=*p;
        }
    }
}
int main(){
    int i,number[10],*p;
    p=number;
    printf("please input 10 number\n");
    for(i=0;i<10;i++){
        scanf("%d",p++);
    }
    p=number;
    max_min_value(p,10);
    printf("mAX=%d,min=%d",max,min);
}