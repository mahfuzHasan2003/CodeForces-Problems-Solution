event_num = int(input())
inp_list = list(map(int, input().split()))
reserved_police, count_untreated = 0,0
for i in inp_list:
    if i==-1 and reserved_police==0:
        count_untreated+=1
    else:
        reserved_police+=i
print(count_untreated)