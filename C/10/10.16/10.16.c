#include<stdio.h>
void inv(int x[],int n){
    int temp,i,j,m=(n-1)/2;
    for(i=0;i<=m;i++){
        j=n-1-i;
        temp=x[i];
        x[i]=x[j];
        x[j]=temp;
    }
}
int main(){
    int i,a[10]={8,3,1,3,4,64,2,24,34,2};
    printf("the original arrayis \n");
    for ( i = 0; i < 10; i++)
    {
        printf("%d ",a[i]);
    }
    inv(a,10);
    printf("\nthe interted arrayis \n");
    for ( i = 0; i < 10; i++)
    {
        printf("%d ",a[i]);
    }
    
}