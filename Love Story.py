case_num = int(input())
str1 = "codeforces"
for i in range(case_num) :
    str2 = input()
    count_differs = 0
    for j in range(len(str2)) :
        if str2[j] != str1[j] :
            count_differs+=1
    print(count_differs)