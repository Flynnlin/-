#include<stdio.h> 
#include<string.h>
main(){
	char st[20],cs[5][20];
	int i,j,p;
	printf("please input 5 name,will order by ascll\n");
	for(i=0;i<5;i++){
		scanf("%s",cs[i]);
	}
	for(i=0;i<5;i++){
		for(j=i+1;j<5;j++){
			if(strcmp(cs[i],cs[j])==1){
				strcpy(st,cs[j]);
				strcpy(cs[j],cs[i]);
				strcpy(cs[i],st);
			}
		}
	}
	for(i=0;i<5;i++){
		printf("%s   ",cs[i]);
	}
}
