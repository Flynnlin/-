#define SSSV(s1,s2,s3,v) s1=l*w;s2=l*h;s3=w*h;v=w*l*h;
#include<stdio.h>
int main(){
    int l=3,w=4,h=5,sa,sb,sc,vv;
    SSSV(sa,sb,sc,vv);
    printf("sa=%d\nsb=%d\nsc=%d\nvv=%d",sa,sb,sc,vv);
}
