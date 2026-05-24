n = int(input())
list1 = list(map(int, input().split()))

untreated = 0
flag = 0

for items in list1:
    if items==-1:
        if flag>0:
            flag-=1
        else:
            untreated += 1
    else:
        flag+=items
print(untreated)
