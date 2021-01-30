#include<stdio.h>
main(){
	char c;
	while(c!='\n'){
		c=getchar();
		if(c==0X1B){
			continue;
		}
		printf("%c\n",c);
	}
} 
