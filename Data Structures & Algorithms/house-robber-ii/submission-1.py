class Solution:
    def robHelper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, n+2, ....]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 0):
            return 0
        if (n == 1):
            return nums[0]
        v1 = self.robHelper(nums[1:])
        v2 = self.robHelper(nums[:n-1])
        return max(v1, v2)