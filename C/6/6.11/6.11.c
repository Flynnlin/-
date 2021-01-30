#include<stdio.h>
main(){
	int x,i;
	printf("please input a interger number  ");
	scanf("%d",&x);
	for(i=x-1;i>1;i--){
		if(x%i==0){
			printf("this is not Prime numbe");
			break;
		}
	}
	if(i==1){
		printf("this is  Prime numbe");
	}
} 
