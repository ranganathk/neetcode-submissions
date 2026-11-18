class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if (r == m-1 or c == n-1):
                    res[r][c] = 1
                else:
                    res[r][c] = res[r+1][c] + res[r][c+1]

        return res[0][0]