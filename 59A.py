s= str(input())
upper = 0
lower = 0
for words in s:
    if words.isupper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(s.upper())
else:
    print(s.lower())
    