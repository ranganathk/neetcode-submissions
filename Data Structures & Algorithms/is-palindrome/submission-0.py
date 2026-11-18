class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join([char.lower() for char in s if char.isalnum()])
        str_len = len(res)
        for l in range(str_len//2):
            if res[l] != res[str_len - l - 1]:
                return False
        
        return True