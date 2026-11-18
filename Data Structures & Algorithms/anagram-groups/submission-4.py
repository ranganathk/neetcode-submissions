class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagram_map[key].append(s)
        return list(anagram_map.values())