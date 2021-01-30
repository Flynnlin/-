#include <stdio.h>
int main(){
    FILE *fp;
    char ch;
    if((fp=fopen("1.txt","wt+"))==NULL){
        printf("can not open file");
    }else
    {
        printf("input a string:\n");
        ch=getchar();
        while (ch!='\n')
        {
            fputc(ch,fp);
            ch=getchar();
        }
       
        
    }
     fclose(fp);
}