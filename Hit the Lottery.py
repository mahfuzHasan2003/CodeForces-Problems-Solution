balance = int(input())
counter = 0
while balance != 0 :
    if balance >= 100 :
        counter += (balance // 100)
        balance %= 100
    elif balance >= 20 :
        counter += (balance // 20)
        balance %= 20
    elif balance >= 10 :
        counter += (balance // 10)
        balance %= 10
    elif balance >= 5 :
        counter += (balance // 5)
        balance %= 5
    elif balance >= 1 :
        counter += (balance // 1)
        balance %= 1
print(counter)


# Time limit exceeded on test 3
# balance = int(input())
# counter = 0
# while balance != 0 :
#     if balance >= 100 :
#         balance -= 100
#     elif balance >= 20 :
#         balance -= 20
#     elif balance >= 10 :
#         balance -= 10
#     elif balance >= 5 :
#         balance -= 5
#     elif balance >= 1 :
#         balance -= 1
#     counter += 1
# print(counter)
