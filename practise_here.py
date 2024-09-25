# def print_rec (n) :
#     if n == 0 :
#         return
#     print_rec(n-1)
#     print(n)
# print_rec(5)

# from Team import count

# loop_num = int(input())
# base = ""
# power = ""
# for i in range(loop_num) :
#     num = input()
#     base = num[0:2]
#     power = num[2:]
#     if (power[0]=="0") or (int(power)<=1) or (int(base)!=10) :
#         print("NO")
#     else :
#         print("YES")

# arr = [15, 29, 37, 22, 16, 5, 26, 31, 6, 32, 19, 3, 45, 36, 33, 14, 25, 20, 48, 7, 42, 11, 24, 28, 9, 18, 8, 21, 47, 17, 38, 40, 44, 4, 35, 1, 43, 39, 41, 27, 12, 13]
# arr.sort(reverse=True)
# print(arr)

n1 = 0
n2 = 10
while n1 <= n2:
    print(n1, n2)
    n1 += 1
    n2 -= 1