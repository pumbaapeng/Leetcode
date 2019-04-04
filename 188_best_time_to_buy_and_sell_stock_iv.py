class Solution:
    def maxProfit(self, k, prices):
        K = min(len(prices) // 2, k)
        best_buy_prev = [float('-inf')] * K  # best cash (could be negative) after the k-th buy
        best_sale_prev = [0] * K  # best cash after the k-th sale
        for price in prices:
            best_buy = [float('-inf')] * K
            best_sale = [0] * K
            for k in range(K):
                best_sale[k] = max(best_sale_prev[k], best_buy_prev[k] + price)
                best_prior_cash = best_sale_prev[k - 1] if k >= 1 else 0
                best_buy[k] = max(best_buy_prev[k], best_prior_cash - price)
            best_buy_prev, best_sale_prev = best_buy, best_sale
        return max(best_sale_prev)


if __name__ == '__main__':
    prices = [3,2,6,5,0,3]
    k = 2
    print(Solution().maxProfit(k, prices))
