#include<stdio.h> 
main(){
	int k;
	static char st1[15],st2[]="C language";
	printf("please input a string\n");
	gets(st1);
	k=strcmp(st1,st2);
	switch(k){
		case 0:{
			printf("st1=st2");
			break;
		}
		case 1:{
			printf("st1>st2");
			break;
		}
		case -1:{
			printf("st1<st2");
			break;
		}
	}
	printf("\n%dby ascll",k);
	
}
