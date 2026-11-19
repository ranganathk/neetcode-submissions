class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 0):
            return 0
        if (N == 1):
            return nums[0]
        
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
         