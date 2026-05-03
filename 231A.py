a= int (input())
output =0
for i in range(a):
    
    x,y,z = map(int,input().split())
    if x+y+z >= 2:
        output += 1
print(output)
            


