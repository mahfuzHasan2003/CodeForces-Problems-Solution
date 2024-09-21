n = int(input())
value = 0
for i in range(n) :
    statement = input()
    if statement == "X++" or statement == "++X":
        value+=1
    elif statement == "X--" or statement == "--X":
        value-=1
print(value)