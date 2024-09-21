year = int(input())
while len(set(str(year))) < 4 :
    year += 1
print(year)