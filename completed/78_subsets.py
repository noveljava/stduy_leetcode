from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List = []
        result.append([])

        MAX_LOOP = len(nums)

        def backtracking(start, info):
            for i in range(start, MAX_LOOP):
                value = nums[i]
                result.append(info+[value])
                backtracking(i+1, info+[value])


        backtracking(0, [])

        return result

print(Solution().subsets([0]))