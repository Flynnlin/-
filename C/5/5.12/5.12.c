#include<stdio.h> 
main(){
	float a,b;
	char c;
	printf("input expression:  a+b:  ");
	scanf("%f%c%f",&a,&c,&b);
	switch(c){
		case '+':{
			printf("a+b=%f",a+b);
			break;
		}
		case '-':{
			printf("a-b=%f",a-b);
			break;
		}
		case '*':{
			printf("a*b=%f",a*b);
			break;
		}
		case '/':{
			printf("a/b=%f",a/b);
			break;
		}
	}
}
