from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [num for num, count in Counter(nums).most_common(k)]


nums = [1,2,3]
k = 2
print(Solution().topKFrequent(nums, 2))