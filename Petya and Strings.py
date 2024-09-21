# Way 1 comparing with each alphabet Unicode value

# word1 = input().lower()
# word2 = input().lower()
# if word1 == word2 :
#     print(0)
# else :
#     for i in range(len(word1)) :
#         if ord(word1[i]) > ord(word2[i]) :
#             print(1)
#             break
#         elif ord(word1[i]) < ord(word2[i]) :
#             print(-1)
#             break


# Way 2 storing all english alphabet and their value then compare

data = {
    "A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5, "F" : 6, "G" : 7, "H" : 8, "I" : 9,
    "J" : 10, "K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15, "P" : 16, "Q" : 17,
    "R" : 18, "S" : 19, "T" : 20, "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25, "Z" : 26
    }

word1 = input().upper()
word2 = input().upper()
if word1 == word2 :
    print(0)
else :
    for i in range(len(word1)) :
        if data[word1[i]] > data[word2[i]] :
            print(1)
            break
        elif data[word1[i]] < data[word2[i]] :
            print(-1)
            break