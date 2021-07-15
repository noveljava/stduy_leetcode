from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List = []
        candidates = sorted(candidates)

        def trace(info):
            for i in candidates:
                current_sum = sum(info)
                if current_sum+i == target:
                    info.append(i)
                    sorted_info = sorted(info)
                    if sorted_info not in result:
                        result.append(sorted_info[:])

                    info.pop()
                elif current_sum+i < target:
                    info.append(i)
                    trace(info)
                    info.pop()
                else:
                    break
        
        trace([])
        return result

candidates = [2,3,6,7]
target = 7

print(Solution().combinationSum(candidates, target))