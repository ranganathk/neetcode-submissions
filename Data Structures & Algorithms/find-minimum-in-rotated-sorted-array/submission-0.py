class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Check if the array is in order?
        # Find the minimum using the start end and middle
        n = len(nums)
        if (nums[0] < nums[n-1]):
            return nums[0]

        lt = 0
        rt = n - 1

        while (lt <= rt):
            mid = (lt + rt)//2

            if (nums[lt] > nums[mid]):
                rt = mid
            else: 
                lt = mid + 1
        
        return nums[rt]
