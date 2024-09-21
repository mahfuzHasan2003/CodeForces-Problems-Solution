inp = list(map(int, input().split("+")))
inp = sorted(inp)
sorted_seq = ""
for i in range(len(inp)) :
    sorted_seq += str(inp[i])
    if i != len(inp)-1 :
        sorted_seq += "+"
print(sorted_seq)