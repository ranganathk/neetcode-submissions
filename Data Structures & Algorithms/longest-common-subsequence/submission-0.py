class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)  # 3 rows, 4 columns

        matrix = [[0 for _ in range(m)] for _ in range(n)]

        def dfs(r, c):
            if (r >= n or c >= m):
                return 0
            
            if (text1[r] == text2[c]):
                val = 1 + dfs(r+1, c+1)
            else:
                val = max(dfs(r+1, c), dfs(r, c+1 ))
            
            matrix[r][c] = val
            return val
        dfs(0, 0)

        return matrix[0][0]