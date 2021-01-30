#include<stdio.h>
int main(){
    FILE *fp;
    char ch;
    if((fp=fopen("1.txt","rt"))==NULL){
        printf("Can nor open file");
    }else
    {
        ch=fgetc(fp);
        while (ch!=EOF)
        {
            putchar(ch);
            ch=fgetc(fp);
        }
    }
    fclose(fp);
    
}