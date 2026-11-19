class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)  # 3 rows, 4 columns

        matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for r in range(n - 1, -1, -1):
            for c in range(m-1, -1, -1):
                if (text1[r] == text2[c]):
                    matrix[r][c] = 1 + matrix[r+1][c+1]
                else:
                    matrix[r][c] = max(matrix[r+1][c], matrix[r][c+1])
        
        return matrix[0][0]