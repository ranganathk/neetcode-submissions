class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i, cur):
            if (i >= len(nums)):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            temp = i
            while (temp+1  < len(nums) and nums[temp] == nums[temp+1]):
                temp += 1

            dfs(temp+1, cur)
        
        dfs(0, [])
        return res