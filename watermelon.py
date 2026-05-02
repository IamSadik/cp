a = int(input())
if a % 2==0 and (a-(a/2)) % 2 == 0:
    print("YES")

elif a%2==0:
    flag =0
    for i in range(2,a):
        for j in reversed(range(2,a)):
            if i % 2 == 0 and j%2==0 and (i + j) == a:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

