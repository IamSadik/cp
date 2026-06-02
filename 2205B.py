import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    x = n
    ans = 1

    p = 2
    while p * p <= x:
        if x % p == 0:
            ans *= p
            while x % p == 0:
                x //= p
        p += 1

    if x > 1:
        ans *= x

    print(ans)