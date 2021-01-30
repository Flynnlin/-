#include<stdio.h>
int main(){
    struct stu
    {
        /* data */
        int num;
        char *name;
        char sex;
        float score;
    }boy2,boy1={102,"zhsn pin",'m',34};
    boy2=boy1;
     printf("%d:%s's sex is %c,Score is %f",boy1.num,boy1.name,boy1.sex,boy1.score);
    
}