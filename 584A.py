n,t = map(int,input().split())

import random

a = 10 ** (n-1)

if n == 1 and t == 10:
    print(-1)
else:
    number = random.randint(a, a*10-1)

    while (number%t!=0):
        number = random.randint(a, a*10-1)

    print(number)