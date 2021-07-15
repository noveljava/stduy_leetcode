from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = nums[0]
        result = prev_sum

        for i, num in enumerate(nums[1:]):
            if prev_sum+num < num:    
                prev_sum = num
            else:
                prev_sum += num
            
            result = max(prev_sum, result)

        return result

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

nums = [-2,1]
print(Solution().maxSubArray(nums))

nums = [1, 2]
print(Solution().maxSubArray(nums))

nums = [-1,0,-2]
print(Solution().maxSubArray(nums))