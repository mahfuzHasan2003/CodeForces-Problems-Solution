coordinates = list(map(int, input().split()))
coordinates.sort()
print((coordinates[1]-coordinates[0])+(coordinates[2]-coordinates[1]))