#include<stdio.h>
#include<math.h>
main(){
	int i;
	float pi=1,j=3;
	for(i=1;i<=10000;i++){
		pi=pi+1/(j*pow(-1,i));
		printf("%d:PI=%10.6lf\n",i,pi*4.0);
		j=j+2;
	}
} 
