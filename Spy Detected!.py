def checkIndex(arr):
    for num in arr:
        if arr.count(num) == 1:
            return arr.index(num)+1
        
for i in range(int(input())):
    arr_len = int(input())
    print(checkIndex(list(map(int, input().split()))))