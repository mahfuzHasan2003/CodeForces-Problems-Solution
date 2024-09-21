num_of_contest = int(input())
coder_points = list(map(int, input().split()))
min_point, max_point = coder_points[0], coder_points[0]
count_amazing = 0
for point in coder_points:
    if min_point < point:
        count_amazing += 1
        min_point = point
    elif max_point > point:
        count_amazing += 1
        max_point = point
print(count_amazing)