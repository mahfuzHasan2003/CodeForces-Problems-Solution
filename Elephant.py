x = int(input())
counter = 0
if x%5 == 0 :
    counter += (x//5)
else :
    counter += (x//5)+1
print(counter)