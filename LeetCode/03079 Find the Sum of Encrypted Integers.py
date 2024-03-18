from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            num_str = str(num) 
            encrypt = int(max(num_str))*len(num_str)
            ans += encrypt
        return ans