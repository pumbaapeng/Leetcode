# key idea: two pass, one from front, and the other from behind
class Solution(object):
    def maxProfit(self, prices):
        max_profit_1st = []
        cur_min = float('inf')
        cur_max_profit = 0 
        for price in prices:
            cur_max_profit = max(price - cur_min, cur_max_profit)
            max_profit_1st.append(cur_max_profit)
            cur_min = min(price, cur_min)
        cur_max = float('-inf')
        max_profit_2nd = 0                                                 
        max_profit = 0 
        for i in xrange(len(prices) - 1, 0, -1):
            price = prices[i]
            max_profit_2nd = max(cur_max - price, max_profit_2nd)
            max_profit = max(max_profit_1st[i - 1] + max_profit_2nd, max_profit)
            cur_max = max(price, cur_max)
        return max(max_profit, max_profit_1st[-1] if len(max_profit_1st) > 0 else 0) # NOTE: note this, i.e.,MAX profit of two OR one transaction
