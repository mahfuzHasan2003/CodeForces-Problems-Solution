friends = int(input())
gift_to = list(map(int, input().split()))
gift_from = []
for i in range(1, friends+1) :
    gift_from.append(str(gift_to.index(i)+1))
print(" ".join(gift_from))