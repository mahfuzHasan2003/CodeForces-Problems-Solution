word = input()
lower_letters = 0
upper_letters = 0
for i in word :
    if i.isupper() == True :
        upper_letters += 1
    else :
        lower_letters += 1
if lower_letters >= upper_letters :
    print(word.lower())
else :
    print(word.upper())