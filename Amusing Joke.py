guest_name = input()
host_name = input()
shuffled_name = sorted(input())
guest_host_sorted = sorted(guest_name+host_name)
if guest_host_sorted == shuffled_name :
    print("YES")
else :
    print("NO")