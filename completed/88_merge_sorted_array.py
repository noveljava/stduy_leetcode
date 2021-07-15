from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result_info = sorted(nums1[:m]+nums2[:n])
        for i, e in enumerate(result_info):
            nums1[i] = e

        return nums1[:m+n]
        

nums1 = [1,2,3,4,5,6,7]
m = 4
nums2 = [2,5,6]
n=3

print(Solution().merge(nums1, m, nums2, n))