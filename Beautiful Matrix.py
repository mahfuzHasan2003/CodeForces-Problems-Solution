matrix = []
x1, y1 = 0, 0
for i in range(5) :
    row = list(map(int, input().split()))
    matrix.append(row)
for i in matrix :
    for value in i :
        if value == 1 :
            x1, y1 = matrix.index(i) + 1, i.index(value) + 1
print(abs(x1-3) + abs(y1-3))
