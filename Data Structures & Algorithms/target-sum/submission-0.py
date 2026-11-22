class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, cur_sum):
            if ((i, cur_sum) in cache):
                return cache[(i, cur_sum)]
            if (i == len(nums)):
                if cur_sum == target:
                    return 1
                return 0

            val = dfs(i+1, cur_sum + nums[i]) + dfs(i+1, cur_sum - nums[i])
            cache[(i, cur_sum)] = val
            return val

        return dfs(0, 0)