#include<stdio.h>
main(){
	int a,b;
	printf("input two numbers:");
	scanf("%d%d",&a,&b);
	if (a>b){
		printf("max=%d\n",a);
	}
	else{
		printf("max=%d\n",b);
	}
} 
