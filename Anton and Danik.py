n  = int(input())
s = input()
Ant, Dan = 0, 0
for i in s :
    if i == "A" :
        Ant += 1
    else :
        Dan += 1
if Ant > Dan :
    print("Anton")
elif Ant < Dan :
    print("Danik")
else :
    print("Friendship")