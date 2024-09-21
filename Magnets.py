a = int(input())
ans= 0
b = '00'
for i in range(a):
    x  = input()
    if x != b:
        ans = ans+1
        b = x
print(ans)