#include <stdio.h>
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
    int i,c=0;
    float ave,s=0;
    for(i=0;i<3;i++){
        s+=boy[i].score;
    }
    printf("the sum=%f,ave=%f",s,s/3);
}