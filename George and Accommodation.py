rooms = int(input())
count_rooms = 0
for i in range(rooms) :
    people_have, capacity = map(int, input().split())
    if capacity - people_have >= 2 :
        count_rooms += 1
print(count_rooms)