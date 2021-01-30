#include<stdio.h>
main(){
	int a,b,max;
	printf("\n input two number  ");
	scanf("%d%d",&a,&b);
	max=a;
	if(max<b)max=b;
	printf("max=%d",max); 
} 
