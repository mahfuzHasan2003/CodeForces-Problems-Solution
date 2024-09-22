arr_len = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
Sereja_point, Dima_point = 0, 0
for i in range(arr_len):
    if i%2 == 0: Sereja_point += arr[i]
    else: Dima_point += arr[i]
print(Sereja_point, Dima_point)