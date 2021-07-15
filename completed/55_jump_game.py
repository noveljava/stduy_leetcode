from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums)-1

        for position in range(len(nums)-1, -1, -1):
            if nums[position] + position > last_position:
                last_position = position

        return last_position == 0

    # time exceed algorithm
    def canJump_yet(self, nums: List[int]) -> bool:
        can_hold = [False] * len(nums)
        can_hold[0] = True
        goal = len(nums)-1

        for i in range(goal):
            if can_hold[i] is False:
                continue

            start = 0 if i-nums[i] < 0 else i-nums[i]
            end = i+nums[i] if i+nums[i] < goal else goal
            for j in range(start, end+1):
                can_hold[j] = True

        return sum(can_hold) == len(nums)


# parameter = [[[2,3,1,1,4], True],
# [[0,2,3], False],
# [[0], True],
# [[2,1,1,0,2], False],
# [[2,5,0,0,3], True]]

# for param, expected in parameter:
#     print(param)
#     assert expected == Solution().canJump(param)


nums = [2, 5, 0, 0, 3]
print(Solution().canJump(nums))
