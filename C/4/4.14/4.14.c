#include<stdio.h>
#include<math.h>
main(){
	float a,b,c,s,area;
	scanf("%f %f %f",&a,&b,&c);
	s=1.0/2*(a+b+c);
	area=sqrt(s*(s-a)*(s-b)*(s-c));
	printf("a=%f,b=%f,c=%f",a,b,c);
	printf("\narea=%f",area);
	 
} 
