from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 중복된 값들을 제거하고, 정렬을 한 뒤 이어져있는 최대 길이값을 구한다.

        if len(nums) == 0:
            return 0

        nums = sorted(list(set(nums)))
        result = 1
        max_length = 1
        for i, v in enumerate(nums[:-1]):
            if v+1 == nums[i+1]:
                max_length += 1
            else:
                result = max(result, max_length)
                max_length = 1

        return max(result, max_length)


if __name__ == '__main__':
    assert 4 == Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    assert 9 == Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
