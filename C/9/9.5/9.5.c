#define SQ(y) (y)*(y)
main(){
	int a,sq;
	printf("input a number:  \n");
	scanf("%d",&a);
	sq=SQ(a+1);
	printf("sq=%d\n",sq);
} 
