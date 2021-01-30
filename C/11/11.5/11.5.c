#include<stdio.h>
struct stu
{
    /* data */
    int num;
    char *name;
    char sex;
    float score;
}boy1={102,"zsdf",'M',43},*pstu;
int main(){
    pstu=&boy1;
    printf("number=%d,Name=%s",(*pstu).num,(*pstu).name);
}
