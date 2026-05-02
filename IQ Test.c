#include<stdio.h>
int main(){
int n,i,cp=0,cn=0,indexp=0,indexn=0;
scanf("%d",&n);
int a[n];
for(i=0;i<n;i++)
{
    scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
 if(a[i]%2==0){
        cp=cp+1;
        indexp=i+1;
 }
 else
  {
    cn=cn+1;
    indexn=i+1;
  }
}
if(cp==1)
    printf("%d",indexp);
else
    printf("%d",indexn);
}
