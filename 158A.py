participant, kth_place = map(int, input().split())

list1 = list(map(int, input().split()))

score = list1[kth_place - 1]

count = 0
for x in list1:
    if x >= score and x > 0:
        count += 1

print(count)