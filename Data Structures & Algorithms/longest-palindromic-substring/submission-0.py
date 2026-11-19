class Solution:
    def isPali(self, s, l, r):
        while (l < r):
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        max_sub_str = 1
        n = len(s)
        for i in range(n-1):
            for j in range(i+1, n):
                if self.isPali(s, i, j):
                    if (j - i + 1) > max_sub_str:
                        max_sub_str = j - i + 1
                        res = s[i:j+1]
        
        return res
