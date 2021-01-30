#include<stdio.h>
main(){
	int n;
	printf("input number\n");
	scanf("%d",&n);
	s(n);
	printf("final n=%d\n",n);
} 
int s(int n){
	int i;
	for(i=n-1;i>=1;i--){
		n=n+i;
	}
	printf("ss n =%d\n",n);
}
