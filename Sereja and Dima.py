arr_len = int(input())
arr = list(map(int, input().split()))
Sereja_point, Dima_point = 0, 0
initial, end = 0, len(arr)-1
count = 1
while initial <= end:
    if count%2 != 0:
        if arr[initial] <= arr[end]:
            Sereja_point += arr[end]
            end-=1
        else:
            Sereja_point += arr[initial]
            initial+=1
    else:
        if arr[initial] <= arr[end]:
            Dima_point += arr[end]
            end-=1
        else:
            Dima_point += arr[initial]
            initial+=1
    count+=1
print(Sereja_point, Dima_point)


