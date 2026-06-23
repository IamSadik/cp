n, m = map(int, input().split())

bulbs = set()
for _ in range(n):
    data = list(map(int, input().split()))
    bulbs.update(data[1:])

if len(bulbs) == m:
    print("YES")
else:
    print("NO")