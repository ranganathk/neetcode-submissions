class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}

        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            if s1[i] in s1_hash:
                s1_hash[s1[i]] += 1
            else:
                s1_hash[s1[i]] = 1

        
        s2_initial_hash = {}

        for j in range(len(s1)):
            if s2[j] in s2_initial_hash:
                s2_initial_hash[s2[j]] += 1
            else:
                s2_initial_hash[s2[j]] = 1
        
        if (s2_initial_hash == s1_hash):
            return True

        for k in range(len(s1), len(s2)):
            if (s2_initial_hash == s1_hash):
                return True
            else:
                window_start = k - len(s1)
                s2_initial_hash[s2[window_start]] -= 1
                if (s2_initial_hash[s2[window_start]] == 0):
                    s2_initial_hash.pop(s2[window_start], None)
                if s2[k] in s2_initial_hash:
                    s2_initial_hash[s2[k]] += 1
                else:
                    s2_initial_hash[s2[k]] = 1               
        
        if (s2_initial_hash == s1_hash):
            return True 

        return False
