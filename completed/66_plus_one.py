from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        max_len = len(digits)
        overflow = 1

        for i in range(max_len-1, -1, -1):
            overflow, val = divmod(digits[i]+overflow, 10)
            digits[i] = val

        if overflow != 0:
            digits.insert(0, overflow)

        return digits

digits = [9,9,9]
print(Solution().plusOne(digits))
