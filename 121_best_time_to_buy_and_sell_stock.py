class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_so_far = float('inf')
        for i,v in enumerate(prices):
            max_profit = max(v - min_so_far, max_profit)
            min_so_far = min(v, min_so_far)
        return max_profit
            
        
