from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 성능 개구림... - -
        max_loop = len(nums)
        for i in range(max_loop):
            for j in range(max_loop):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        print(nums)


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)