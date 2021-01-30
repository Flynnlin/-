#include<stdio.h>
main(){
	int x=100,i;
	printf("100-200 Prime number  \n\n");
	for(;x<200;x++){
		for(i=x-1;i>1;i--){
			if(x%i==0){
/*				printf("%d is not Prime numbe\n",x);*/
				break;
			}
		}
		if(i==1){
			printf("%d is  Prime numbe\n",x);
		}
	}
} 
