class Solution:
    @staticmethod
    def remove_smallest(array):
        for j in range(len(array) - 1):
            if array[j + 1] - array[j] > 1:
                return False
        return True


test_cases = int(input())
for i in range(test_cases):
    arr_len = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if Solution.remove_smallest(arr):
        print("YES")
    else:
        print("NO")