# better way
n = int(input())
coins = list(map(int, input().split()))
coins.sort()
x = []
while sum(x) <= sum(coins):
    x.append(coins.pop())
print(len(x))


# worst way
# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort(reverse=True)
# initial_sum = 0
# counter = 1
# half_of_coins = sum(coins) / 2
# for i in range(len(coins)) :
#     initial_sum += coins[i]
#     if initial_sum <= half_of_coins :
#         counter += 1
# print(counter)


