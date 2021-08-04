from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        result = [0 for _ in range(len(nums))]
        result[0] = nums[0]
        result[1] = nums[1]
        result[2] = result[0] + nums[2]

        for i in range(3, len(nums)):
            result[i] = nums[i] + max(result[i-3], result[i-2])

        return max(result)


assert Solution().rob([1]) == 1
assert Solution().rob([1, 2]) == 2
assert Solution().rob([1, 2, 3]) == 4

assert Solution().rob([1, 2, 3, 1]) == 4
assert Solution().rob([2, 7, 9, 3, 1]) == 12
assert Solution().rob([7, 1, 3, 9, 2]) == 16
assert Solution().rob([1, 7, 3, 2, 9]) == 16
