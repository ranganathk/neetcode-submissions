class Solution:
    def minEle(self, nums: List[int], lt: int, rt:int, target: int) -> int:
        left = lt
        right = rt - 1
        while (left <= right):
            mid = (left+right)//2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1

        return -1
    

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if (nums[0] < nums[n-1]):
            return self.minEle(nums, 0, n, target)

        lt = 0
        rt = n - 1

        while (lt < rt):
            mid = (lt + rt)//2

            if (nums[mid]> nums[rt]):
                lt = mid + 1
            else: 
                rt = mid
    
        # Minimum is nums[lt]
        print(lt)
        print(nums[0], nums[lt - 1], nums[lt], nums[n-1])

        if (target >= nums[0] and target <= nums[lt - 1]):
            return self.minEle(nums, 0, lt, target)
        elif (target >= nums[lt] and target <= nums[n-1]):
            return self.minEle(nums, lt, n, target)
        else:
            return -1    
        