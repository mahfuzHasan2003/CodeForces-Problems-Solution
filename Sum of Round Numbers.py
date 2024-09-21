class Solution:
    def __init__(self, inp):
        self.inp = inp
    def round_solver(self):
        out_array = []
        for k in range(len(str(self.inp))):
            if str(self.inp)[k] != "0":
                out_array.append(str(self.inp)[k] + (len(str(self.inp))-(k+1))*"0")
        print(len(out_array))
        print(* out_array)

test_cases = int(input())
for i in range(test_cases):
    user_inp = int(input())
    obj = Solution(user_inp)
    obj.round_solver()