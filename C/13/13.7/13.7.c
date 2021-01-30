#include<stdio.h>
struct student{
    char name[10];
    int num;
}boy;
int main(){
    FILE *fp;
    char ch;
    struct student *pp;
    if((fp=fopen("1.txt","wt+"))==NULL){
        printf("can nor open file");
    }else
    {
        printf("please type a num ,a name to add to file\n");
        scanf("%d %s",&boy.num,&boy.name);
        fprintf(fp,"%d %s",boy.num,boy.name);
        printf("write ok\n");
        rewind(fp);
        fscanf(fp,"%d %s",&pp->num,&pp->name);
        printf("data is %d   %s",pp->num,pp->name);
}
}