class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        arr = []

        for i in range(n-2):
            l = i + 1
            r = n - 1
            while (l < r):
                curr_sum = nums[i] + nums[l] + nums[r]
                if (curr_sum == 0):
                    arr.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif (curr_sum < 0):
                    l += 1
                else:
                    r -= 1
        
        second_hash = {}
        for ar in arr:
            ar.sort()
            key = '-'.join(map(str, ar))
            second_hash[key] = ar

        result = []
        for a, b in second_hash.items():
            result.append(b)
        
        return result