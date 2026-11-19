class Solution:
    def isValidSubs(self, arr_s: List[int], arr_t: List[int]) -> bool:
        for i in range(len(arr_s)):
            if arr_t[i] > arr_s[i]:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        n_t = len(t)
        n_s = len(s)
        if n_s < n_t:
            return ""
        arr_s = [0]*128        
        arr_t = [0]*128
        min_subs_l = n_s
        min_str = s

        for i in range(n_t):
            arr_t[ord(t[i])] += 1
            
        start = 0
        end = 0
        while (end < n_s):
            arr_s[ord(s[end])] += 1
            loop_entered = False
            loop_counter = 0
            while self.isValidSubs(arr_s, arr_t):
                # Run reducer to make it invalid
                # Update the length of the 
                current_str = s[start:end+1]
                if (len(current_str) < min_subs_l):
                    min_str = current_str
                    min_subs_l = len(current_str)
                
                loop_entered = True
                loop_counter += 1
                arr_s[ord(s[start])] -= 1
                start += 1

            if loop_entered:
                start += 1
            else: 
                end += 1
            
        return min_str    
        
