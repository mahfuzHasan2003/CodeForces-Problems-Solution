import math
for i in range(int(input())):
    a, b = map(int, input().split())
    dif = abs(a-b)
    print(math.ceil(dif/10))