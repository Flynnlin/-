#define SQ(y) ((y)*(y))
main(){
	int i=1;
	while(i<=5){
		printf("%d:%d\n",i,SQ(i++));
	}
} 
