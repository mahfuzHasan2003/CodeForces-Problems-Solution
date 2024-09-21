def check_good_str(inp_str) :
    count_a = 0
    count_b = 0
    for i in range(len(inp_str)) :
        if inp_str[i] == "A" :
            count_a+=1
        else :
            count_b+=1
        if count_b > count_a :
            return "NO"
    if inp_str[0] == "B" or inp_str[-1] == "A" :
        return "NO"
    else :
        return "YES"

test_case = int(input())
for i in range(test_case) :
    inp = input()
    print(check_good_str(inp))


# def check_good_str(inp) :
#     count_A = inp.count("A")
#     count_B = inp.count("B")
#     if count_B > count_A or inp[0] == "B" or inp[-1] == "A" :
#          return "NO"
#     return "YES"
 
# test_case = int(input())
# for i in range(test_case) :
#     inp = input()
#     print(check_good_str(inp))