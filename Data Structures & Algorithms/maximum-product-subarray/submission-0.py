class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            
            tmp1 = cur_max * n
            tmp2 = cur_min * n
            cur_max, cur_min = max(tmp1, tmp2, n), min(tmp1, tmp2, n)

            res = max(res, cur_max)

        return res    
        
        

        