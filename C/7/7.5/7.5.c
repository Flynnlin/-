#include<stdio.h>
main(){
	int i,j,p,q,s,a[10];
	printf("\n input 10 numbers:");
	for(i=0;i<10;i++){
		scanf("%d",&a[i]);
	}
	for(i=0;i<10;i++){
		p=i;
		q=a[i];
		for(j=i+1;j<10;j++){
			if(q<a[j]){
				p=j;
				q=a[j];
			}
			if(i!=p){
				s=a[i];
				a[i]=a[p];
				a[p]=s;
			}
		} 
	printf("%d\n",a[i]);	
	}
} 
