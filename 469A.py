n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))



p=x[1:]
q=y[1:]

p.sort()
q.sort()

total = set(p) | set(q)

for i in range(1, n + 1):
    if i not in total:
        print("Oh, my keyboard!")
        break
else:
    print("I become the guy.")