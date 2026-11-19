class Solution:
    def curentWindowMax(self, nums: List[int], start: int, end: int) -> int:
        current_max = nums[start]
        for i in range(start, end):
            current_max = max(current_max, nums[i])

        return current_max

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n - k + 1):
            current_max = self.curentWindowMax(nums, i, i + k)
            result.append(current_max)
        
        return result
        
