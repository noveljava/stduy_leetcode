from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import defaultdict
        max_loop = len(nums)
        
        hash_map =  defaultdict(int)
        i = 0

        while i < max_loop and nums[i] is not None:
            current_value = nums[i]
            if hash_map[current_value] < 2:
                hash_map[current_value] += 1
            elif current_value == nums[i-1]:
                for j in range(i, max_loop-1):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

                nums[-1] = None
                i -= 1

            i += 1

        return sum(hash_map.values())

nums = [1,1,1,1]
print(Solution().removeDuplicates(nums))