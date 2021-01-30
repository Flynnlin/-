#include<stdio.h>
struct student{
    char name[10];
    int num;
    int age;
    char addr[15];
}boy;
int main(){
    FILE *fp;
    char ch;
    struct student *pp;
    if((fp=fopen("1.txt","wt+"))==NULL){
        printf("can nor open file");
    }else
    {
        printf("please type a num ,a name ,an age,an address to add to file\n");
        scanf("%d %s %d %s",&boy.num,&boy.name,&boy.age,&boy.addr);
        fwrite(&boy,sizeof(struct student),2,fp);
        rewind(fp);
        fread(pp,sizeof(struct student),2,fp);
        printf("\ndata:%d %s %d %s",pp->num,pp->name,pp->age,pp->addr);
    }
}