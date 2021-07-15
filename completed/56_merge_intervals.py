from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result: List = []
        intervals = sorted(intervals, key=lambda x: x[0])

        goal = len(intervals)

        item = intervals[0]
        i = 1

        while i < goal:
            diff_item = intervals[i]
            if item[0] <= diff_item[0] <= item[1]:
                start = min(item[0], diff_item[0])
                end = max(item[1], diff_item[1])
                item = [start, end]
            else:
                result.append(item)
                item = diff_item
            
            i += 1

        result.append(item)
        return result

# intervals = [[8,10],[1,3],[15,18],[2,6]]
intervals = [[1,4], [4,5]]
print(Solution().merge(intervals))