#include<stdlib.h>
#include <stdio.h>
void main(){
    FILE *fp1,*fp2;
    char ch;
    printf("f1 copy to f2");

    
    if((fp1=fopen("1.txt","rt"))==NULL ){
        printf("can not open file");
        printf("%d",11);
    }else
    {
        fp2=fopen("2.txt","wt+");
        ch=fgetc(fp1);
        while (ch!=EOF)
        {
            fputc(ch,fp2);
            printf("%c",ch);
            ch=fgetc(fp1);
        }
        fclose(fp1);
        fclose(fp2);
    }
    printf("\n\nok");
    
}