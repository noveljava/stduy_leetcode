from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        MAX_Y = len(obstacleGrid)
        MAX_X = len(obstacleGrid[0])

        for y in range(MAX_Y):
            for x in range(MAX_X):
                if obstacleGrid[y][x] == 1:
                    # 갈 수 없는 길이다. 계산을 할 필요가 없다. 그리고 옆에 얘들한테 영향을 주면 안된다.
                    obstacleGrid[y][x] = 0
                else:
                    top = obstacleGrid[y-1][x] if y != 0 else 0
                    left = obstacleGrid[y][x-1] if x != 0 else 0

                    if x == 0 and y == 0:
                        obstacleGrid[y][x] = 1
                    else:
                        obstacleGrid[y][x] = top+left

        return obstacleGrid[MAX_Y-1][MAX_X-1]


# obstacleGrid = [[0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,1,0,0],[0,0,1,0,0]]
obstacleGrid = [[0,1],[0,0]]
# obstacleGrid = [[1,0],[0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))