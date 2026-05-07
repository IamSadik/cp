str1= input()
str1= str1.lower()


str2= input()
str2= str2.lower()

flag=0

for i in range(len(str1)):
    if str1[i] != str2[i]:
        if str1[i] > str2[i]:
            print(1)
            flag=1
            break
        elif str1[i] < str2[i]: 
            print(-1)
            flag=1
            break
    
if flag == 0:
    print(0)
