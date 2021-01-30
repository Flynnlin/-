#include <stdio.h>
void main(){
    enum week{
        dun,mon,tu3,erf,thu,fri,dst
    }a,b,c;
    a=dun;
    b=mon;
    c=tu3;
    printf("%d %d  %d",a,b,c);
}