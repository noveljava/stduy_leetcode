from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List = []

        def tracking(info):
            if len(info) == len(nums):
                result.append(info[:])
                return

            for i in nums:
                if i not in info:
                    info.append(i)
                    tracking(info)
                    info.pop()

        tracking([])

        return result


nums = [1, 2, 3]
print(Solution().permute(nums))
