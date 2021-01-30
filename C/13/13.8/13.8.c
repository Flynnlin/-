#include<stdio.h>
struct student{
    char name[10];
    int num;
}boy;
int main(){
    FILE *fp;
    char ch;
    struct student *pp;
    if((fp=fopen("1.txt","at+"))==NULL){
        printf("can nor open file");
    }else
    {
        printf("please type a num ,a name to add to file\n");
        scanf("%d %s",&boy.num,&boy.name);
        fprintf(fp,"%d %s\n",boy.num,boy.name);
        printf("write ok\n");
        fseek(fp,0,0);
        fscanf(fp,"%d %s\n",&pp->num,&pp->name);
        printf("data is %d   %s",pp->num,pp->name);
}
}