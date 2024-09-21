test_cases = int(input())
for i in range(test_cases) :
    Alice, Bob = map(int, input().split())
    if (Alice+Bob)%2 == 0 :
        print("Bob")
    else :
        print("Alice")


# # top worst case and will get an error
# test_cases = int(input())
# for i in range(test_cases) :
#     Alice, Bob = map(int, input().split())
#     while True:
#         if Alice < Bob :
#             Alice, Bob = Bob, Alice
#         Alice-=1
#         if Alice > Bob :
#             Alice, Bob = Bob, Alice
#         Bob-=1
#         if Alice == 0 or Bob == 0 :
#             break
#     if (Alice == 0 and Bob == 0) or (Alice == 0 and Bob != 0) :
#         print("Bob")
#     if Alice != 0 and Bob == 0 :
#         print("Alice")