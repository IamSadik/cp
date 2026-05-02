#include<iostream>
using namespace std;
int main(){
int a,b,c;
cin>>a>>b>>c;
int largest,smallest,median;
if(a>b&&a>c){
    largest=a;
}
else if(b>a&&b>c){
    largest=b;
}
else
    largest=c;
if(a<b&&a<c){
    smallest=a;
}
else if(b<a&&b<c){
    smallest=b;
}
else
    smallest=c;
for(int i=0;i<3;i++){
if(a!=largest&&a!=smallest){
    median=a;
}
else if(b!=largest&&b!=smallest){
    median=b;
}
else
median=c;
}
if(smallest!=1)
cout<<largest*(median*smallest);
else if(smallest==1&&largest==1&&median==1)
    cout<<largest+smallest+median;
else
    cout<<largest*(median+smallest);
}
