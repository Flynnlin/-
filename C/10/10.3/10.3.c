#include<stdio.h>
void swap(int *p1,int *p2){
    int temp;
    temp=*p1;
    *p1=*p2;
    *p2=temp;
}
int main(){
    int a,b;
    int *pointer1,*pointer2;
    printf("please input 2 number\n");
    scanf("%d%d",&a,&b);
    pointer1=&a;
    pointer2=&b;
    if(a<b){
        swap(pointer1,pointer2);
    }
    printf("%d %d\n",*pointer1,*pointer2);
}