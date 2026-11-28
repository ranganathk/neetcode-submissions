class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)  # 3 rows, 4 columns

        matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            matrix[n-i][m] = i
        
        for j in range(m+1):
            matrix[n][m-j] = j
        
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                if (word1[r] == word2[c]):
                    matrix[r][c] = matrix[r+1][c+1]
                else:
                    matrix[r][c] = 1 + min(matrix[r+1][c],matrix[r][c+1], matrix[r+1][c+1])
        
        return matrix[0][0]