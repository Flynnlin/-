#include<stdio.h>
void nzp(int v){
	if(v>0){
		printf("--%d\n",v);
	}else{
		printf("--%d\n",0);
	}
}
main(){
	int a[5],i;
	printf("input 5 numbers\n");
	for(i=0;i<5;i++){
		scanf("%d",&a[i]);
		nzp(a[i]);
	}
	
} 
