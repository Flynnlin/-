#include<stdio.h>
main(){
	int i,j,p,s,a[11]={127,3,54,32,45,23,45,6,23,65,76};
	for(i=0;i<11;i++){
		for(j=i+1;j<11;j++){
			if(a[i]>a[j]){
				p=a[j];
				a[j]=a[i];
				a[i]=p;
			}
		}
	}
	for(i=0;i<11;i++){
		printf("%d  ",a[i]);
	} 
	printf("please type a num:");
	scanf("%d",&s);
	for(i=0;i<=11;i++){
		if(s<a[i]){
			break;
		}
	}
	p=i;
	for(i=11;i>p;i--){
		a[i]=a[i-1];
	}
	a[p]=s;
	for(i=0;i<=11;i++){
		printf("%d  ",a[i]);
	} 
	
} 
