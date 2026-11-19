class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buy or Sell
        # If Buy -> i + 1
        # If Sell -> i + 2
        dp = {} # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if (i >= len(prices)):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                buy = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, True)
                val = max(buy, cooldown)
                dp[(i, True)] = val
            else:
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False)
                val = max(sell, cooldown)
                dp[(i, False)] = val
            return val
        
        return dfs(0, True)
                


            
            

        





