test_cases = int(input())
for i in range(test_cases) :
    n = int(input())
    if n < 3 :
        print(0)
    else :
        print(n//2-1 if n%2==0 else n//2)