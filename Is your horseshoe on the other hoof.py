colors_list = list(map(int, input().split()))
colors_set = set(colors_list)
print(len(colors_list) - len(colors_set))