class Solution:
    def isValidSubs(self, arr_s: List[int], arr_t: List[int]) -> bool:
        for i in range(len(arr_s)):
            if arr_t[i] > arr_s[i]:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        n_s = len(s)
        n_t = len(t)
        
        arr_s = [0] * 256
        arr_t = [0] * 256

        for i in range(len(t)):
            arr_t[ord(t[i])] += 1
        
        left = 0
        right = 0
        min_len = math.inf
        min_start = 0 

        while right < n_s:
            arr_s[ord(s[right])] += 1
            
            while self.isValidSubs(arr_s, arr_t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove s[left] from the current window
                arr_s[ord(s[left])] -= 1
                left += 1
            
            right += 1
        
        if min_len == math.inf:
            return ""
        
        return s[min_start:min_start + min_len]