#include<stdio.h>
int main(){
    struct stu
    {
        int num;
        char *name;
        char sex;
        float score;
    }boy1,boy2;
    boy1.num=102;
    boy1.name="zhnsping";
    printf("please input sex,and score\n");
    scanf("%c %f",&boy1.sex,&boy1.score);
    printf("%d:%s's sex is %c,Score is %f",boy1.num,boy1.name,boy1.sex,boy1.score);
    
}