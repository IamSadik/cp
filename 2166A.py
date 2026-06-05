t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    target = s[-1]
    ops = 0
    for i in range(n - 1):
        if s[i] != target:
            ops += 1
            
    print(ops)