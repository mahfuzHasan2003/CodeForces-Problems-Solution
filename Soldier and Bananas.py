price, balance, quantity = map(int, input().split())
total_price = 0
for i in range(1, quantity+1) :
    total_price += (price*i)
ans = (total_price - balance)
if ans < 0:
    print(0)
else:
    print(ans)
