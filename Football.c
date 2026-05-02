#include<stdio.h>
#include<string.h>
int main(){
char a[101];
gets(a);
int i,count=0;
int l=strlen(a);
for(i=0;i<=l;i++)
{
    if(a[i]=='0')
    {
        count=count+1;
        if(count==7)
        {
            break;
        }
    }
    else
        count=0;
}
if(count==7)
    printf("YES");
else
{
    for(i=0;i<=l;i++)
{
    if(a[i]=='1')
    {
        count=count+1;
         if(count==7)
        {
            break;
        }
    }
    else
        count=0;
}
if(count==7)
    printf("YES");
else
    printf("NO");
}

}
