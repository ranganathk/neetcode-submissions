class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        val = amount
        res = 0
        for c in coins:
            res += val // c 
            val = val % c
        
        if val == 0:
            return res

        return -1 