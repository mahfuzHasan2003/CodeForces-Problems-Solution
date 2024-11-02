column_num = int(input())
cubes_in_col = list(map(int, input().split()))
cubes_in_col.sort()
print(" ".join(str(x) for x in cubes_in_col))