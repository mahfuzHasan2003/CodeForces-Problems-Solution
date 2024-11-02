def check_user_input(inp) :
    is_produce_output = False
    instruction = ["H", "Q", "9"]
    for i in inp:
        if i in instruction:
            is_produce_output = True
            return is_produce_output
    return is_produce_output

inp = input()
if check_user_input(inp):
    print("YES")
else:
    print("NO")