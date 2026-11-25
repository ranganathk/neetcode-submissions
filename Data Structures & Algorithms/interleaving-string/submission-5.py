class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        res = [[False]*(n+1) for _ in range(m+1)]
        res[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i < m and s3[i+j] == s1[i] and res[i+1][j]:
                    res[i][j] = True 
                if j < n and s3[i+j] == s2[j] and res[i][j+1]:
                    res[i][j] = True
        
        return res[0][0]