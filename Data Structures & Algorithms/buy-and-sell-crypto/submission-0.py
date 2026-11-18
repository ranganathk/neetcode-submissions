class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_cost = prices[0]
        profit = 0
        for i in range(n):
            
            buy_cost = min(buy_cost, prices[i])
            profit = max(profit, prices[i] - buy_cost)
        
        return profit