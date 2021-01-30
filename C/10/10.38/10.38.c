#include<stdio.h>
int main(int argc,char *argv){
    if(argc==1){
        printf("please 带参");
    }else
    {
        while(argc-->1){
            printf("%s\n",*++argv);
        }
    }
    
}