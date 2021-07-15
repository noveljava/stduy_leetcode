from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 단순 검색 매우 느리다.
        for i in range(len(nums)):
            if target == nums[i]:
                return True

        return False

    # 내장 함수 사용.
    def search_using_func(self, nums: List[int], target: int) -> bool:
        # 정렬하고 검색하면 더 빠르지롱 !
        sorted(nums)

        try:
            nums.index(target)
            return True
        except:
            return False

nums = [2,5,6,0,0,1,2]
target = 3
print(Solution().search(nums, target))