#include<stdio.h>
int main(){
    char st[20],*ps;
    int i;
    printf("input a string\n");
    ps=st;
    scanf("%s",ps);
    for(i=0;ps[i]!='\0';i++){
        if(ps[i]=='k'){
            printf("thers is a k \n");
            break;
        }
    }
    if(ps[i]=='\0'){
        printf("there is no k");
    }
}