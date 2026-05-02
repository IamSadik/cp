#include<stdio.h>
int main(){
int i=0,count=0;
long long int a;
scanf("%lld",&a);
while(a>0){
if(a%10==4||a%10==7)
{
    count++;
}
a/=10;
}
if(count==4||count==7)
    printf("YES");
else
    printf("NO");

}
