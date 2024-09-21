test_cases = int(input())
for i in range(test_cases) :
    num, divisor = map(int, input().split())
    if num%divisor == 0 :
        print(0)
    else :
        print(divisor-(num%divisor))