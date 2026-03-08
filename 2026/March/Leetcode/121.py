class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
            if min_price > prices[i]:
                min_price = prices[i]
        return max_profit

test_case_01 = [7,1,5,3,6,4]
test_case_02 = [7,6,4,3,1]

s = Solution()

print(s.maxProfit(test_case_01))
print(s.maxProfit(test_case_02))