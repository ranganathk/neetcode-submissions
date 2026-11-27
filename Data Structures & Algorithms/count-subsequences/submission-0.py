class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)  # 3 rows, 4 columns

        cache = {}

        def dfs(r, c):
            if (c >= m):
                return 1
            if (r >= n):
                return 0    
            if (r, c) in cache:
                return cache[(r, c)]
            
            if (s[r] == t[c]):
                val = dfs(r+1, c+1) + dfs(r+1, c)
            else:
                val = dfs(r+1, c)
            
            cache[(r, c)] = val
            return val
        
        return dfs(0, 0)

         