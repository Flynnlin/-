#include<stdio.h>
void sort(int x[],int n){
    int i,j,k,t,s;
    for(i=0;i<n-1;i++){
        k=i;
        for(j=i+1;j<n;j++){//找到最大的那一个
            if(x[j]>x[k]){
                k=j;
            }
        }
        if(k!=i){
            t=x[i];
            x[i]=x[k];
            x[k]=t;
        }
        for(s=0;s<10;s++){
            printf("--%d ",x[s]);
        }
        printf("\n");
    }
}
int main(){
    int *p,i,a[10]={23,34,1,32,454,2,23,342,45,23};
    printf("The original array:\n");
    for(i=0;i<10;i++){
        printf("%d,",a[i]);
    }
    p=a;
    printf("\n the iner arrat;\n");
    sort(p,10);
    for(i=0;i<10;i++){
        printf("%d ",*p);
        p++;
    }
}