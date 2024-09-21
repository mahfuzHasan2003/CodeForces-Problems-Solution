user_word_range = int(input())
user_inp = set(map(str, input().lower()))
if len(user_inp) == 26 :
    print("YES")
else :
    print("NO")