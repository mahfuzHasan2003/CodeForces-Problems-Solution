def makeSum(one_part):
    sum = 0
    for i in one_part: sum += int(i)
    return sum

for i in range(int(input())):
    ticket_no = input()
    if makeSum(ticket_no[:3]) == makeSum(ticket_no[3:]): print("YES")
    else: print("NO")
    