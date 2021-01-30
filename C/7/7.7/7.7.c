#include<stdio.h>
main(){
		int i,j,s=0,average,v[3];
		int a[5][3]={{80,23,12},{12,32,12},{23,1,31},{23,43,54},{34,34,54}};
	printf(" 15 scores\n");
	for(i=0;i<3;i++){
		for(j=0;j<5;j++){
			s=s+a[j][i];
		}
		v[i]=s/5;
		s=0; 
	}
	average=(v[0]+v[1]+v[2])/3; 
	printf("math:%d\tlanguag:%d\tdbase:%d\t\n",v[0],v[1],v[2]);
	printf("the total average is:%d\n",average) ;
} 
