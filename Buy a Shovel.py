class Solution:
    @staticmethod
    def find_min_to_buy(price, retail):
        min_buy = 1
        while True:
            if (price*min_buy)%10 == 0 or (price*min_buy)%10 == retail:
                return min_buy
            min_buy += 1


shovel_price, retail_coin = map(int, input().split())
print(Solution.find_min_to_buy(shovel_price, retail_coin))