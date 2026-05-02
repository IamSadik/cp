#include<iostream>
using namespace std;
int main(  ){
string a;
cin>>a;
int i,flag=0;
for(i=0;i<100;i++){
    if(a[i]=='H'||a[i]=='Q'||a[i]=='9'){
        flag++;
    }
}
if(flag>0)
   cout<<"YES";
else if (flag==0)
   cout<<"NO";
}
