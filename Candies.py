import math
for i in range(int(input())):
    total_candy_wrappers = int(input())
    maximum_day = math.floor(math.log2(total_candy_wrappers+1))
    # series_last_number = int(math.pow(2, maximum_day-1))
    # series_sum = 2*series_last_number - 1
    for i in range(2, maximum_day+1):
        series_sum = 2*int(math.pow(2, i-1)) - 1
        if(total_candy_wrappers%series_sum == 0):
            print(total_candy_wrappers//series_sum)
            break