#include<stdio.h>
int main(  ){
char a[100];
scanf("%s",&a);
int i,flag=0;
for(i=0;i<100;i++){
    if(a[i]=='H'||a[i]=='Q'||a[i]=='9'){
        flag++;
    }
}
if(flag>0)
    printf("YES");
else if (flag==0)
    printf("NO");
}
