#include <stdio.h>
int main(){
    char *name[]={
        "Tollow me","BASIC","GREAT","FOR","COM"
    };
    char **p;
    int i=0;
    for(i=0;i<5;i++){
        p=name+i;
        printf("%s\n",*p);
    }
}