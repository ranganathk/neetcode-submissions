class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        my_hash = {}
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        arr = [nums[i], nums[j], nums[k]]
                        arr.sort()
                        key = '-'.join(map(str, arr))
                        my_hash[key] = arr
        
        arrs = []
        for key, value in my_hash.items():
            arrs.append(value)
        
        return arrs