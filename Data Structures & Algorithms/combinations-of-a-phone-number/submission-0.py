class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        
        def dfs(i, cur):
            if (len(digits) == 0):
                return
            if (i >= len(digits)):  
                res.append(cur)
                return
            
            letters = mapping[digits[i]]

            for j in range(len(letters)):
                dfs(i + 1, cur + letters[j])
            
        dfs(0, "")

        return res
