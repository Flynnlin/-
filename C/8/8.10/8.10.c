void nzp(int a[8]){
	int i;
	printf("\nvalues of array a are:\n");
	for(i=0;i<8;i++){
		if(a[i]<0){
			a[i]=0;
		}
		printf("%d\n",a[i]);
	}
} 
void main(){
	int b[5],i;
	printf("\ninput 5 numbers:\n");
	for(i=0;i<5;i++){
		scanf("%d",&b[i]);
	}
	printf("initial values of array b are:\n");
	for(i=0;i<5;i++){
		printf("%d ",b[i]);
	}
	nzp(b);
	printf("\n last values of array b are:\n ");
	for(i=0;i<5;i++){
		printf("%d ",b[i]);
	}
}
