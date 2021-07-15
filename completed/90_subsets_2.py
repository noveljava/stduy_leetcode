from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        nums.sort()
        def backtracking(start, info):
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                info.append(nums[i])
                if info[:] not in result:
                    result.append(info[:])

                backtracking(i+1, info)
                info.pop()

        
        backtracking(0, [])
        return result

nums = [4,4,4,1,4]
print(Solution().subsetsWithDup(nums))
