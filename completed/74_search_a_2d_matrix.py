from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        MAX_ROW = len(matrix)
        MAX_COLUMN = len(matrix[0])

        find_row = -1
        # 이것도 바이너리 서치로 구현이 가능.
        top = 0
        bottom = MAX_ROW-1
        
        while top <= bottom:
            position = (top+bottom) // 2
            if matrix[position][0] == target:
                return True
            elif matrix[position][MAX_COLUMN-1] == target:
                return True
            elif matrix[position][0] < target < matrix[position][MAX_COLUMN-1]:
                find_row = position
                break
            elif matrix[position][0] < target:
                top = position + 1
            elif matrix[position][0] > target:
                bottom = position -1

        if find_row == -1:
            return False
        
        # binary search
        left = 0
        right = MAX_COLUMN-1
        result = -1

        while left<=right:
            position = (left+right) // 2
            if matrix[find_row][position] == target:
                result = position
                break
            elif matrix[find_row][position] < target:
                left = position + 1
            else:
                right = position -1


        return result != -1

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

print(Solution().searchMatrix(matrix, target))