def solve():
    s = input()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 1
    return len(s)
 
test_cases = int(input())
for i in range(test_cases):
    print(solve())
