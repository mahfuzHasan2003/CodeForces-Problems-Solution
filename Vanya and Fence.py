friends, fence_height = map(int, (input().split()))
friends_height = map(int, (input().split()))
min_width = 0
for i in friends_height :
    if i <= fence_height :
        min_width += 1
    else :
        min_width += 2
print(min_width)