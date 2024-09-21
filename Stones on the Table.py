n = int(input())
stones = list(input())
counter = 0
for i in range(len(stones)-1) :
    if stones[i] == stones[i+1] :
        counter+=1
print(counter)