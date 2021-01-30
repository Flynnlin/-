#include <stdio.h>
#include <stdlib.h>
int main(){
    int i;
    char *day_name(int n);
    printf("input Day No:\n");
    scanf("%d",&i);
    if(i<0){
        exit(1);
    }
    printf("Day No:%2d--%s\n",i,day_name(i));
}
char *day_name(int n){
    static char *name[]={
        "IIIegal day",
        "Monday",
        "tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    };
    return ((n<1||n>7)?name[0]:name[n]);
}