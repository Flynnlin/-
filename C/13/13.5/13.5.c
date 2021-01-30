#include<stdio.h>
int main(){
    FILE *fp;
    char ch,st[20];
    if((fp=fopen("1.txt","at+"))==NULL){
        printf("can nor open file");
    }else
    {
        printf("please type a string to add to file\n");
        scanf("%s",st);
        fputs(st,fp);
        printf("add is done");
    }
    
}