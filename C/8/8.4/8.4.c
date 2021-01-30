#include<stdio.h>
long f1(long p){
	return p*p;
}
long f2(float q){
	long s=0;
	for(q;q>=0;q--){
		s=s+q;
	}
	return s;
}
main(){
	float s=0;
	s=f2(f1(2))+f2(f1(3));
	printf("%lf",s);
} 
