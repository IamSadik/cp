t = int(input())

max_a = 0
max_count = 0
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_count = a.count(max_a)

    print(max_count)
    