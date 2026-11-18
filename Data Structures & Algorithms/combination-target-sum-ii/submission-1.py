class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if (total == target):
                if cur not in res:
                    res.append(cur.copy())
                return
            if (i >= len(candidates) or total > target):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
            temp = i
            while (temp+1  < len(candidates) and candidates[temp] == candidates[temp+1]):
                temp += 1

            dfs(temp+1, cur, total)
        
        dfs(0, [], 0)
        return res

        