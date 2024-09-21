layer = int(input())
his_feelings = ""
for i in range(1, layer+1) :
    if i%2 != 0 :
        his_feelings += "I hate "
    else :
        his_feelings += "I love "
    if i != layer :
        his_feelings += "that "
his_feelings += "it"
print(his_feelings)