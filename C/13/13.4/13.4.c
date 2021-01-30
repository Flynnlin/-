#include<stdlib.h>
#include<stdio.h>
int main(){
    FILE *fp;
    char str[11];
    if((fp=fopen("1.txt","rt"))==NULL){
        printf("can not open file");
    }else
    {
        fgets(str,11,fp);
        printf("%s",str);
        fclose(fp);
    }
    
}