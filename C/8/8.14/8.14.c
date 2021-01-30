#include<stdio.h>
int a=3,b=5;
max(int a,int b){
	int c;
	c=a>b?a:b;
	return(c);
}
main(){
	int a=8;
	printf("%d\n",max(a,b));
}
