#include<stdio.h>
main(){
	int a[][4]={3,16,87,43,2,45,33,456,34,56,34,23};
	int b[3],i,j,l;
	for(i=0;i<=2;i++){
		b[i]=a[i][0];
		for(j=0;j<=3;j++){
			if(b[i]<a[i][j]){
				b[i]=a[i][j];
			}
		}
		printf("%d\n",b[i]);
	}
} 
