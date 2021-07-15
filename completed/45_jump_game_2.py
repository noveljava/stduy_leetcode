from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        last_position = len(nums)-1
        jump_count = [last_position] * len(nums)
        jump_count[-1] = 0
        
        for position in range(len(nums)-2, -1, -1):
            available = nums[position]+1
            jump_count[position] = min(jump_count[position:position+available])+1

        return jump_count[0]


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
