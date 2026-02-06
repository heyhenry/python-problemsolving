# Leetcode No.121: Best Time to Buy and Sell Stock
# More Info: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    # def maxProfit(self, prices: list[int]) -> int:
    #     size = len(prices)
    #     best_price = 0
    #     for i in range(size):
    #         for j in range(i+1, size):
    #             profit = prices[j] - prices[i]
    #             if profit > best_price:
    #                 best_price = profit
    #     print(best_price)
    #     return best_price

    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        profit = 0
        best_price = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            if profit > best_price:
                best_price = profit
            if min_price > prices[i]:
                min_price = prices[i]
        print(best_price)
        return best_price

test_case_01 = [7,1,5,3,6,4]
test_case_02 = [7,6,4,3,1]

s = Solution()

s.maxProfit(test_case_01)
s.maxProfit(test_case_02)

