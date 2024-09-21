test_cases = int(input())
for i in range(test_cases):
    num_list = list(map(int, input().split()))
    if sum(num_list)/2 in num_list: print("YES")
    else: print("NO")