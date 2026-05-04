n = int(input())
output = 0

for i in range(n):
    x,y,z= map(int,input().split())
    if(x,y,z=='+'):
        output += 1
    else:
        output -= 1

print(output)
