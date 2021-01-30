#include<stdio.h>
struct stu
{
    /* data */
    int num;
    char *name;
    char sex;
    float score;
}boy[3]={
    {101,"lo",'m',33},
    {301,"fdlo",'m',33},
    {801,"lso",'m',33},
};
int main(){
    struct stu *ps;
    for(ps=boy;ps<boy+3;ps++){
        printf("num:%d\tname:%s\tsex:%c\n",ps->num,ps->name,ps->sex);
    }
}