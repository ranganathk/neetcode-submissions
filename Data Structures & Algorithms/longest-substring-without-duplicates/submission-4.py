class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if (n == 0 or n == 1):
            return n
        
        l = 0
        r = 0
        res = 0
        alphabets = [False]*128

        while (r < n):

            while (alphabets[ord(s[r])] == True):
                alphabets[ord(s[l])] = False
                l += 1

            alphabets[ord(s[r])] = True

            res = max(res, (r - l + 1))
            r += 1

        return res