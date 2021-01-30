#include <stdio.h>
struct stu
{
    /* data */
    int num;
    char *name;
    char sex;
    float score;
}boy[3]={
    {101,"lo",'m',3.3},
    {301,"fdlo",'m',3.3},
    {801,"lso",'m',33.4}
};
int main(){
    struct stu *ps;
    void ave(struct stu *ps);
    ps=boy;
    ave(ps);
}
void ave(struct stu *ps){
    int c=0,i;
    float ave,s=0;
    for(i=0;i<3;i++,ps++){
        s+=ps->score;
    }
    printf("average is %f",s/3.0);
}