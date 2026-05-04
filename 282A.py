n = int(input())
output = 0

for i in range(n):
    str1 = input()
    if '+' in str1:
        output += 1
    else:
        output -= 1

print(output)
            
        
