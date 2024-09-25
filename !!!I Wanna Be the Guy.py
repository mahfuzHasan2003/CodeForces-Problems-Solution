game_level = int(input())
x_pass = list(map(int, input().split()))
y_pass = list(map(int, input().split()))
total_pass = set(x_pass + y_pass)

if max(total_pass) == game_level:
    if len(total_pass) == game_level or (0 in total_pass and len(total_pass)-1 == game_level):
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")
else :
    print("Oh, my keyboard!")

# wrong test 12
# if len(total_pass) == game_level :
#     print("I become the guy.")
# else :
#     print("Oh, my keyboard!")

# wrong test 6
# if game_level in total_pass:
#     print("I become the guy.")
# else:
#     print("Oh, my keyboard!")