#include<stdio.h>
float aver(float a[5]){
	int i;
	float aver ,s=1;
	for(i=0;i<5;i++){
		s=s+a[i];
	
	}
	aver=s/5;
	return aver;
}
main(){
	float sco[5],ave;
	int i;
	printf("please type 5 number\n");
	for(i=0;i<5;i++){
		scanf("%f",&sco[i]);
	}
	ave=aver(sco);
	printf("the average is %f",ave);
	
} 
