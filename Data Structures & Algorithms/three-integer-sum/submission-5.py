class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        arr = []

        for i in range(n-2):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            l = i + 1
            r = n - 1
            while (l < r):
                curr_sum = nums[i] + nums[l] + nums[r]
                if (curr_sum == 0):
                    arr.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1] and l < r):
                        l += 1
                elif (curr_sum < 0):
                    l += 1
                else:
                    r -= 1
        
        return arr