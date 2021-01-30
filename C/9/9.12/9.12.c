#include<stdio.h>
#define NUM ok
main(){
    struct stu{
        int num;
        char *name;
        char sex;
        float score;
    }*ps;
    ps=(struct stu*)malloc(sizeof(struct stu));
    ps->num=102;
    ps->name="Zhang ping";
    ps->sex="M";
    ps->score=62.5;
    #ifdef NUM
    printf("NUmber=%d\nScore=%f",ps->num,ps->score);
    #else
    printf("no define num");
    #endif
    free(ps);
}