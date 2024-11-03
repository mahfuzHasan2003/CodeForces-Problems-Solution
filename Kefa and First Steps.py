loop_inp = int(input())
bussiness_amount = list(map(int, input().split()))
current_value = bussiness_amount[0]
non_decreasing = []
count = 0

for i in range(len(bussiness_amount)):
    if bussiness_amount[i] >= current_value:
        count+=1
    else:
        non_decreasing.append(count)
        count = 1
    current_value = bussiness_amount[i]
    if i == len(bussiness_amount) - 1 : non_decreasing.append(count)
print(max(non_decreasing))