a= int (input())
output =0
for i in range(a):
    
    for j in range(1,4):
        count = int(input())
        if j == 1:
            flag = flag + 1
        if flag>=2:
            output = output + 1
        flag = 0

print(output)
            


