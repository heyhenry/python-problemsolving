"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
def maxProfit(prices : list[int]) -> int:

    max_profit = None

    for i in range(len(prices)):
        for j in range(1, len(prices)):
            if max_profit is None and i < j:
                max_profit = prices[j] - prices[i]
            elif prices[j] - prices[i] > max_profit and i < j:
                max_profit = prices[j] - prices[i]

    if max_profit < 1:
        max_profit = 0
    
    return max_profit  
        
def main():
    print(maxProfit([7,1,5,3,6,4])) # 5
    print(maxProfit([7,6,4,3,1])) # 0
    print(maxProfit([3, 8, 2, 10, 5, 1])) # 8
    print(maxProfit([2, 4, 1, 7, 6, 9])) # 8
    print(maxProfit([5, 4, 3, 2, 1])) # 0

if __name__ == "__main__":
    main()