class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}
    
        # Increment count for characters in the first string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            
        # Decrement count for characters in the second string
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
                
        # If the dictionary is empty, all frequencies perfectly matched
        return len(char_count) == 0