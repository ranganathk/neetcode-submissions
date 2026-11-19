class Solution:
    def isAnagram(self, a, b):
        return sorted(a) == sorted(b)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = [False] * n
        res = []

        for i in range(n):
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, n):
                if not visited[j] and self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited[j] = True

            res.append(group)

        return res 

