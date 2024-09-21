loopinp = int(input())
for i in range (loopinp):
    word = input()
    if word == "localization" :
        print("l10n")
    elif word == "internationalization" :
        print("i18n")
    elif len(word) > 10 :
        print(word[0] + str(len(word)-2) + word[-1])
    else :
        print(word)
