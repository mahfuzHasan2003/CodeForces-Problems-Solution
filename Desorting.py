
class MyClass:
    @staticmethod
    def count_min_shuffle(arr_list):
        set_ans = arr_list[-1]
        for i in range(1, len(arr_list)):
            if arr_list[i] >= arr_list[i-1]:
                set_ans = min(set_ans, arr_list[i]-arr_list[i-1])
            else:
                return 0
        return set_ans//2 + 1

obj = MyClass()
test_cases= int(input())
for i in range(test_cases):
    arr_len= int(input())
    inp_list = list(map(int,input().split(' ')))
    print(obj.count_min_shuffle(inp_list))