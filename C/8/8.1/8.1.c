#include<stdio.h>
int max(int a,int b){
	if(a>b){
		return a;
	}else{
		return b;
	}
}
main(){
	int max(int a,int b);
	int x,y,z;
	printf("type 2 numbers  ");
	scanf("%d%d",&x,&y);
	z=max(x,y);
	printf("max=%d",z);
} 
