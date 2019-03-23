class Solution(object):
    def maxProfit(self, prices):
        tot_profit = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                tot_profit += diff
        return tot_profit
