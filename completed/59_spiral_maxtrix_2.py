from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[None for _ in range(n)] for _ in range(n)]
        goal = n*n
        MAX_X, MAX_Y = n, n

        x, y, di = 0, 0, 0
        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        for i in range(goal):
            i = i+1
            result[y][x] = i

            next_y, next_x = y+dy[di], x+dx[di]
            if 0 <= next_y < MAX_Y and 0 <= next_x < MAX_X and result[next_y][next_x] is None:
                y, x = next_y, next_x
            else:
                di = (di+1)%4
                y, x = y+dy[di], x+dx[di]

        return result

print(Solution().generateMatrix(5))
print(Solution().generateMatrix(3))
print(Solution().generateMatrix(1))