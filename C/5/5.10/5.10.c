#include<stdio.h>
main(){
	int a;
	printf("input interger number  ");
	scanf("%d",&a);
	switch(a){
		case 1:{
			printf("Monday  ");
			break;
		}
		case 2:{
			printf("Tuesday  ");
			break;
		}
		case 3:{
			printf("Wednesday  ");
			break;
		}
		case 4:{
			printf("Thursday  ");
			break;
		}
		case 5:{
			printf("Friday  ");
			break;
		}
		case 6:{
			printf("saturday  ");
			break;
		}
		case 7:{
			printf("Sunday  ");
			break;
		}
		default:printf("error a=%d",a);
	}
} 
