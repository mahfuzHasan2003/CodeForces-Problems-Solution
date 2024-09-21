test_cases = int(input())
count = 0
for i in range (test_cases) :
    Petya, Vasya, Tonya = map(int, input().split(" "))
    if (Petya+Vasya+Tonya >= 2) :
        count+=1
print(count)