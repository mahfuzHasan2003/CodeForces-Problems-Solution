inp = list(map(int, input().split()))
inp.sort(reverse=True)
print(inp[0]-inp[1], inp[0]-inp[2], inp[0]-inp[3])