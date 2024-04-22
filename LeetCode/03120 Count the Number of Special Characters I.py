class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lowerbag, upperbag = set(), set()
        diff = ord('a') - ord('A')
        count = 0
        
        for letter in word:
            temp = ord(letter)
            if temp >= ord('a'):
                lowerbag.add(temp)
            else:
                upperbag.add(temp)
        
        for upper in upperbag:
            if upper + diff in lowerbag:
                count += 1
            
        return count