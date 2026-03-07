class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            buying_price = prices[i]
            profit = 0
            for j in range(i+1, len(prices)):
                selling_price = prices[j]
                profit = selling_price - buying_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit

test_case_01 = [7,1,5,3,6,4]
test_case_02 = [7,6,4,3,1]

s = Solution()

print(s.maxProfit(test_case_01))
print(s.maxProfit(test_case_02))