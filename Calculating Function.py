# Time limit exceeded on test 3
# num = int(input())
# func = ""
# for i in range(1, num+1) :
#     if i%2 != 0 :
#         func += ("-"+str(i))
#     else :
#         func += ("+"+str(i))
# print(eval(func))


# Time limit exceeded on test 3
# num = int(input())
# even_sum, odd_sum = 0, 0
# for i in range(1, num+1) :
#     if i%2 == 0 :
#         even_sum += i
#     else :
#         odd_sum += i
# print(even_sum - odd_sum)



num = int(input())
if num%2 != 0 :
    print(-(num+1)//2)
else :
    print(num//2)