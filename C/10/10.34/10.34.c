#include<stdio.h>
#include<stdlib.h>
void main(){
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
    char *ps;
    int i;
    char *day_name(char *name[],int n);
    printf("input DAy NO\n");
    scanf("%d",&i);
    if (i<0){
        exit(1);
    }
    ps=day_name(name,i);
    printf("Day num %2d ==%s",i,ps);
}
char *day_name(char *name[],int n){
    char *pp1,*pp2;
    pp1=*name;
    pp2=*(name+n);
    return ((n<1||n>7)?pp1:pp2);
}