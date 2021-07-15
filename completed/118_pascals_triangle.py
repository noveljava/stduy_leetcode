from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])

        for i in range(1, numRows):
            row_info = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row_info.append(1)
                else:
                    row_info.append(result[i-1][j-1] + result[i-1][j])

            result.append(row_info)

        return result

print(Solution().generate(5))