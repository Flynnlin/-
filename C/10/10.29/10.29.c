#include <stdio.h>
void cpystr(char *pss,char *pds){
    while((*pds=*pss)!='\0'){
        pds++;
        pss++;
    }
}
int main(){
    char *pa="CHINA",b[10],*pd;
    pd=b;
    cpystr(pa,pd);
    printf("string a=%s   b=%s",pa,pd);
}