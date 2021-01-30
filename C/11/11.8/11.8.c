#include<stdio.h>
#include <stdlib.h>
int main(){
    struct stu{
        int num;
        char *name;
        char sex;
        float score;
    } *ps;
    ps=(struct stu*)malloc(sizeof(struct stu));
    ps->num=123;
    ps->name="dsdfd";
    ps->sex='m';
    ps->score=23.0;
    printf("Number=%d\t name %s  sex %c",ps->num,ps->name,ps->sex);
    free(ps);
}