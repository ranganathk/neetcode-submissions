class Solution:
    def isValidSubs(self, arr_s: List[int], arr_t: List[int]) -> bool:
        for i in range(len(arr_s)):
            if arr_t[i] > arr_s[i]:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        n_s = len(s)
        n_t = len(t)
        
        arr_s = [0] * 128
        arr_t = [0] * 128

        for i in range(len(t)):
            arr_t[ord(t[i])] += 1
        
        required = sum(1 for count in arr_t if count > 0)
        have = 0

        left = 0
        right = 0
        min_len = math.inf
        min_start = 0 

        while right < n_s:
            c_right = ord(s[right])
            arr_s[c_right] += 1
            if arr_t[c_right] > 0 and arr_s[c_right] == arr_t[c_right]:
                have += 1
            
            while have == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove s[left] from the current window
                c_left = ord(s[left])
                if arr_t[c_left] > 0 and arr_s[c_left] == arr_t[c_left]:
                    have -= 1
                arr_s[c_left] -= 1
                left += 1
            
            right += 1
        
        if min_len == math.inf:
            return ""
        
        return s[min_start:min_start + min_len]