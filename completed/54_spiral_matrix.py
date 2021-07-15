from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result: list = []
        x = 0
        y = 0

        max_x = len(matrix[0])
        max_y = len(matrix)

        if max_y == 1:
            return matrix[0]

        # 1: right, 2: down, 3: left, 4: up
        direct = 1
        max_count = max_x * max_y
        count = 0

        while matrix[y][x] != None:
            result.append(matrix[y][x])
            matrix[y][x] = None

            if direct == 1:
                if x+1 == max_x or matrix[y][x+1] == None:
                    y += 1
                    direct = 2
                else:
                    x += 1

            elif direct == 2:
                if y+1 == max_y or matrix[y+1][x] == None:
                    x -= 1
                    direct = 3
                else:
                    y += 1

            elif direct == 3:
                if x-1 == -1 or matrix[y][x-1] == None:
                    y -= 1
                    direct = 4
                else:
                    x -= 1

            elif direct == 4:
                if y-1 == -1 or matrix[y-1][x] == None:
                    x += 1
                    direct = 1
                else:
                    y -= 1

        return result
            
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(Solution().spiralOrder(matrix))