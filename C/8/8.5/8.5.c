#include<stdio.h>
int f1(int a){
	int n;
	if(a==1){
		n=1;
	}else{
		n=f1(a-1)+a;
	}
	return n;
} 
main(){
	int x=4;
	printf("%d",f1(x));
}
