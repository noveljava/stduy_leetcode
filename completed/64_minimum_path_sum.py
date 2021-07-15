from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 0 <= grid[i][j] <= 100
        # setting default value = 999.

        MAX_Y = len(grid)
        MAX_X = len(grid[0])

        for y in range(MAX_Y):
            for x in range(MAX_X):
                if x == 0 and y == 0:
                    continue
                
                top = grid[y-1][x] if y != 0 else 999
                left = grid[y][x-1] if x != 0 else 999

                # 위와 왼쪽 중에 작은 값을 선택하여 더한다.
                grid[y][x] += min(top, left)

        return grid[MAX_Y-1][MAX_X-1]

grid = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid))
