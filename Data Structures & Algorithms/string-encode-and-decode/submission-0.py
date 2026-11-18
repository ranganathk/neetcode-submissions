class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        for string in strs:
            encode += str(len(string)) + "#" + string

        return encode

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while (i < len(s)):
            word = ""
            count = 0
            letter_count = ""
            j = i
            while s[j] != "#":
                letter_count += s[j]
                j += 1
            count = int(letter_count) 
            
            j += 1

            while j < i + len(letter_count) + 1 + count:
                word += s[j]
                j += 1
            
            i += len(letter_count) + 1 + count

            words.append(word)

        
        return words
