stops = int(input())
remaining_pass = 0
capacity_list = []
for i in range(stops) :
    exit, enter = map(int, input().split())
    remaining_pass -= exit
    remaining_pass += enter
    capacity_list.append(remaining_pass)
print(max(capacity_list))