# better way
student, time = map(int, input().split())
queue_seq = input()
for i in range(time) :
    queue_seq.replace("BG", "GB")
print(queue_seq)



# top worst way
# students, time = map(int, input().split())
# queue_order = input()
# new_order = []
# for t in range(time) :
#     i = 0
#     while  i+1 <= len(queue_order) :
#         # Grouping where need to be swapped
#         queue_order = list(queue_order)
#         if (i+1 != len(queue_order)) and (queue_order[i] == "B" and queue_order [i+1] == "G") :
#             new_order.append(queue_order[i]+queue_order[i+1])
#             i+=1
#         else :
#             new_order.append(queue_order[i])        
#         i+=1

#     # Swapping their position
#     for j in range(len(new_order)) :
#         if new_order[j] == "BG" :
#             new_order[j] = "GB"
#     queue_order = "".join(new_order)
#     new_order = []

# print(queue_order)