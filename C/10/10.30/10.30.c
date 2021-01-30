#include<stdio.h>
void cpystr(char *pss,char *pds){
    while(*pds++=*pss++);
}
int main(){
    char *pa ="CHINA",b[10],*pb;
    pb=b;
    cpystr(pa,pb);
    printf("string a=%s  b=%s",pa,pb);
}