num = input()
lucky_digit = num.count("4") + num.count("7")
if lucky_digit == 4 or lucky_digit == 7 :
    print("YES")
else :
    print("NO")