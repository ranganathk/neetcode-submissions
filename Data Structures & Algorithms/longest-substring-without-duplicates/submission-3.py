class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)    
        res = 0

        lastIndex = [-1] * 128

    # Initialize start of current window
        start = 0

    # Move end of current window
        for end in range(n):

            start = max(start, lastIndex[ord(s[end])] + 1)

        # Update result if we get a larger window
            res = max(res, end - start + 1)

        # Update last index of s[end]
            lastIndex[ord(s[end])] = end

        return res