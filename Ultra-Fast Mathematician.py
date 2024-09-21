num1 = input()
num2 = input()
ans = ""
for i in range(len(num1)) :
    if num1[i] != num2[i] :
        ans+="1"
    else :
        ans+="0"
print(ans)