class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c, prevVal):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS):
                return 0
            
            if (matrix[r][c] <= prevVal):
                return 0
            
            if (r,c) in cache:
                return cache[(r, c)]
            
            value = 1
            value = max(value, 1 + dfs(r+1, c, matrix[r][c]))
            value = max(value, 1 + dfs(r-1, c, matrix[r][c]))
            value = max(value, 1 + dfs(r, c+1, matrix[r][c]))
            value = max(value, 1 + dfs(r, c-1, matrix[r][c]))
            cache[(r,c)] = value

            return value
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(cache.values())
            