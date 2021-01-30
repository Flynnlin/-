#include<stdio.h>
int max(int x,int y){
	int z;
	z=x>y?x:y;
	return z;
} 
main(){
	extern A,B;
	printf("%d\n",max(A,B));
}
int A=13,B=-8;
