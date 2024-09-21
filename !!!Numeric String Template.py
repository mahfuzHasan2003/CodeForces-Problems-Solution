# check matches the template or not
# def check_match (arr, tm):
#     if len(arr) != len(tm):
#         return "NO"
#     else:
#         # grouping duplicate word's value by following the list 'arr'
#         positions = {}
#         for index, character in enumerate(tm):
#             if character not in positions:
#                 # adding value in a set
#                 positions[character] = {arr[index]}
#             else:
#                 positions[character].add(arr[index])
#         # checking if any of set's length greater than 1 or not
#         for k in positions:
#             if len(positions[k]) > 1:
#                 return "NO"
#         return "YES"
#
#
# # Main code starts here
# test_cases = int(input())
# for i in range(test_cases):
#     array_length = int(input())
#     array_elements = list(map(int, input().split()))
#     template_test_cases = int(input())
#     for j in range(template_test_cases):
#         template = input()
#         print(check_match(array_elements, template))