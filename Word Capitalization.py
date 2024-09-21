word = input()
capitalized_word = ""
for i in range(len(word)) :
    if i == 0 :
        capitalized_word += word[i].upper()
    else :
        capitalized_word += word[i]
print(capitalized_word)