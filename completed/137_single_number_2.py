from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        result = []
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if count[i] == 1:
                result.append(i)
            elif count[i] == 2:
                result.remove(i)

        return result[0]

nums = [2,2,4,2]
print(Solution().singleNumber(nums))