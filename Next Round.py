n, k = map(int, input().split())
scores = list(map(int, input().split()))
cut =scores[k-1]
ans = 0

for i in scores:
    if i >= cut and i > 0:
        ans = ans+1
print(ans)