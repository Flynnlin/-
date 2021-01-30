#include<stdio.h>
main(){
	int n=0;
	char a="";
	printf("input a string:\n");
	while(a!='n'){
		a=getchar();
		printf("   %d\n",a!='n');
		n++;
	}
	printf("%d",n);	
} 
