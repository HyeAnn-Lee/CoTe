class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev = ''.join(list(s)[::-1])
        for i in range(len(s)-1):
            if s[i:i+2] in rev:
                return True
        return False