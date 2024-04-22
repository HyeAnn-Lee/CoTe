import string


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lower, upper = string.ascii_lowercase, string.ascii_uppercase
        count = 0
        
        for i in range(26):
            if upper[i] in word and lower[i] in word:
                count += 1
            
        return count