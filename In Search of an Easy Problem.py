n = int(input())
opinion = map(int, input().split())
is_easy = "Easy"
for i in opinion :
    if i == 1 :
        is_easy = "HARD"
        break
print(is_easy)