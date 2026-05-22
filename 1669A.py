n = int(input())

list1 = []
for i in range(0, n):
    list1.append(int(input()))

for items in list1:
    if items <= 1399:
        print("Division 4")
    elif items <= 1599:
        print("Division 3")
    elif items <= 1899:
        print("Division 2")
    else:
        print("Division 1")