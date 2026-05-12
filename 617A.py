coordinate = int(input())
output = 0
steps= [5,4,3,2,1]


for step in steps:
    while step<=coordinate:
        coordinate=(coordinate-step)
        output+=1
print(output)
 