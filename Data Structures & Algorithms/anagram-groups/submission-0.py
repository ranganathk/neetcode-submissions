class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        return "".join(sorted(str1)) == "".join(sorted(str2))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        seen = [False]*n

        output = []
        for i in range(n):
            if seen[i]:
                continue
            
            group = [strs[i]]
            seen[i] = True
            for j in range(i+1, n):
                if not seen[j] and self.isAnagram(strs[i], strs[j]):
                    group.append(strs[j])
                    seen[j] = True

            output.append(group)
        return output

