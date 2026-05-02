#include<stdio.h>
int main(){
int a[100];
int lvl,i,j,count=0,n;
int b[100];
scanf("%d",&lvl);
scanf("%d",&a[0]);
for(i=1;i<=a[0];i++)
{
    scanf("%d",&a[i]);
}
scanf("%d",&b[0]);
for(i=1;i<=b[0];i++)
{
    scanf("%d",&b[i]);
}
n=a[0]+b[0];
int c[n];
if(n!=0){

for(i=0,j=1;j<=a[0];i++,j++)
{
    c[i]=a[j];
}
for(i,j=1;i<n;i++,j++)
{
    c[i]=b[j];
}
j=0;
for(i=1;i<=1;i++)
    {
        for(j;j<n;)
        {
            if(c[j]==i&&i<=lvl){

                i=i+1;
                count ++;
                j=0;
            }
            else
                j++;
        }
    }

    if (count!=lvl)
        printf("Oh, my keyboard!");
    else
        printf("I become the guy.");

}
else if (n==0)
    printf("Oh, my keyboard!");
}
