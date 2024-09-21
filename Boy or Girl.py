user_name = input()
distinct__chr_list = []
for i in range(len(user_name)) :
    if user_name[i] not in distinct__chr_list :
        distinct__chr_list.append(user_name[i])
if len(distinct__chr_list) % 2 != 0 :
    print("IGNORE HIM!")
else :
    print("CHAT WITH HER!")