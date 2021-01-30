#include<stdio.h>
void swap(int *p1,int *p2){
    int *p;
    p=p1;
    p1=p2;
    p2=p;
}
int main(){
    int a,b;
    int *point1,*point2;
    printf("please input 2 number\n");
    scanf("%d%d",&a,&b);
    point1=&a;
    point2=&b;
    if(a<b){
        swap(point1,point2);
    }
    printf("\n%d,%d\n",*point1,*point2);
}