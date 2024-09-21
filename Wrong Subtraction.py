num, cacl_time = map(int, input().split())
for i in range(cacl_time) :
    if num%10 == 0 :
        num //= 10
    else :
        num -= 1
print(num)