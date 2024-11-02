def check_dangerous(inp):
    if len(inp) < 7: return "NO"
    for i in range(len(inp)-6):
        if inp[i:7+i] == "0000000" or inp[i:7+i] == "1111111": return "YES"
    return "NO"


players = input()
print(check_dangerous(players))