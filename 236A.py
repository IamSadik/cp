name = input()


duplicate_count = len(name) - len(set(name))

length = len(name)-duplicate_count

if length%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
