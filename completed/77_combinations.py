from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List = []

        def backtracking(k, start, stack_result):
            for j in range(start, n+1):
                if k != 1:
                    backtracking(k-1, j+1, stack_result+[j])
                else:
                    result.append(stack_result + [j])

        backtracking(k, 1, [])
        return result

print(Solution().combine(1, 1))

