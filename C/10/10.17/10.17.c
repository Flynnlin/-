#include<stdio.h>
void inc(int *x,int n){
    int *p,temp,*i,*j,m=(n-1)/2;
    i=x;
    j=x+n-1;
    p=x+m;
    for(;i<=p;i++,j--){
        temp=*i;
        *i=*j;
        *j=temp;
    }
}
int main(){
    int i,a[10]={8,3,1,3,4,64,2,24,34,2};
    printf("the original arrayis \n");
    for ( i = 0; i < 10; i++)
    {
        printf("%d ",a[i]);
    }
    inc(a,10);
    printf("\nthe interted arrayis \n");
    for ( i = 0; i < 10; i++)
    {
        printf("%d ",a[i]);
    }
    
}