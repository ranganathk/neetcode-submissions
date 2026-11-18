class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        res = 0

        for num in nums:
            my_set.add(num)
        
        for val in nums:
            if val in my_set and val-1 not in my_set:
                cur = val
                cnt = 0
                while cur in my_set:
                    cur += 1
                    cnt += 1
            
                res = max(cnt, res)
        
        return res