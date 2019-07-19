"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = [0] * len(prices)

        max_profit = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if max_profit < prices[i]:
                max_profit = prices[i]

            profit[i] = max(max_profit - prices[i], profit[i + 1])

        # print(profit)
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            profit[i] = max(profit[i] + prices[i] - min_price, profit[i - 1])

        # print(profit)
        return profit[-1]

if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(Solution().maxProfit(prices))
