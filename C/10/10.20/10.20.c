#include<stdio.h>
void inv(int *x,int n){
    int *p,m,temp,*i,*j;
    m=(n-1)/2;
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
    int i,*p,arr[]={1,3,4,5,7,8,3,4,5,6};
    p=arr;
    printf("the orignal array\n:");
    for(i=0;i<10;i++){
        printf("%d,",arr[i]);
    }
    inv(p,10);
    printf("\nTHe array has been inverted\n");
    for(i=0;i<10;i++,p++){
        printf("%d,",*p);
    }
}