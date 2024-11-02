user_inp = input()
splited_inp = [ i for i in user_inp.split('WUB') if i != ""]
print(" ".join(splited_inp))