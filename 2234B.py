def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

t = int(input())

for _ in range(t):
    n = int(input())

    if n < 22:
        found = False

        for a in range(n + 1):
            if is_palindrome(a) and (n - a) % 12 == 0:
                print(a, n - a)
                found = True
                break

        if not found:
            print(-1)

    else:
        r = n % 12

        if r == 10:
            a = 22
        else:
            a = r

        b = n - a
        print(a, b)
