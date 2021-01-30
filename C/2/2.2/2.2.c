#include <stdio.h>
main(){
	int sigh=1;
	float deno=2.0,sum=1.0,term;
	while(deno<=100){
		sigh=-sigh;
		term=sigh/deno;
		sum=sum+term;
		deno=deno+1;
	}
	printf("%f",sum);
} 
/*Çó¼¶Êý£¿£¿*/ 
