from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start_index = 0
        end_index = 0

        sum_value = 0
        result = 0
        while end_index != len(nums):
            sum_value += nums[end_index]
            end_index += 1

            if sum_value >= target:
                while sum_value - nums[start_index] >= target:
                    sum_value -= nums[start_index]
                    start_index += 1

                result = end_index-start_index if result == 0 else min(result, end_index-start_index)

        return result


if __name__ == '__main__':
    assert 2 == Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
    assert 1 == Solution().minSubArrayLen(target=4, nums=[1, 4, 4])
    assert 0 == Solution().minSubArrayLen(target=11, nums=[1, 4, 4])
    assert 3 == Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5])
    assert 2 == Solution().minSubArrayLen(target=7, nums=[4, 3, 1, 1, 5])
