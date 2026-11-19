class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        i = 0

        while i < len(s):
            if int(s[i]) == 1 or int(s[i] == 2):
                if i + 1 < len(s) and int(s[i+1]) <= 6 and int(s[i+1] != 0):
                    res += 2
                else:
                    res += 1
                i += 2
            elif int(s[i]) == 0:
                return 0
            else:
                res += 1
                i += 1

        return res


             