import math
n, k = map(int, input().split())
half = math.ceil(n/2)
if half >= k : print((2*k) - 1)
else : print((k-half) * 2)
