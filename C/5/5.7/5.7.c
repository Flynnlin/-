#include<stdio.h>
main(){
	int a,b ;
	printf("please input a b>");
	scanf("%d%d",&a,&b);
	if (a==b){
		printf("A=B");
	} else if(a>b){
		printf("A>b");
	}else{
		printf("A<B");
	}
} 
