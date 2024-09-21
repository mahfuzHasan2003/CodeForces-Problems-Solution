user_inp = input()
if user_inp == "{}" :
    print(0)
else :
    print(len(set(user_inp[1:-1].split(", "))))
