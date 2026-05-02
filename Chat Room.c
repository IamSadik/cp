#include<stdio.h>
int main(){
char a[100];
int i,flag=0;
scanf("%s",&a);
for( i=0;i<100;i++){
    if(a[i]=='h'){
        for(i=i+1;i<100;i++){
            if(a[i]=='e'){
                for(i=i+1;i<100;i++){
                    if(a[i]=='l'){
                        for(i=i+1;i<100;i++){
                        if(a[i]=='l'){
                            for(i=i+1;i<100;i++){
                                if(a[i]=='o'){
                                        flag++;
                            printf("YES");
                            goto point;
                                }
                            }
                        }
                        }
                    }
                }
            }
        }
    }
}
point:
if(flag==0)

    printf("NO");
}
