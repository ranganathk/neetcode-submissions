class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)

        if (arr_sum % 2 != 0):
            return False

        target = arr_sum / 2

        totals = set()
        totals.add(0)

        for i in range(len(nums) - 1, -1, -1):
            if target in totals:
                return True
            set_copy = totals.copy()
            for s in set_copy:
                s1 = nums[i] + s 
                totals.add(s1)

        return False        

        
            
