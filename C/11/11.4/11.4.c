#include<stdio.h>
#define NUM 3
struct stu
{
    /* data */
    char name[20];
    char phone[10];
};

int main(){
    struct stu men[NUM];
    int i;
    for(i=0;i<NUM;i++){
        printf("input name:\n");
        gets(men[i].name);
        printf("input phone:\n");
        gets(men[i].phone);
    } 
    for(i=0;i<NUM;i++){
        printf("%s\t\t\t%s\n",men[i].name,men[i].phone);
    }   
   
    
}