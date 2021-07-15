from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # zero_row = []
        # zero_column = []

        # 중복값 제거를 자동으로 해주기때문에 성능이 훨씬 좋다.
        zero_row = set()
        zero_column = set()

        MAX_ROW = len(matrix)
        MAX_COLUMN = len(matrix[0])

        # find information
        for r in range(MAX_ROW):
            for c in range(MAX_COLUMN):
                if matrix[r][c] == 0:
                    # zero_row.append(r)
                    # zero_column.append(c)
                    zero_row.add(r)
                    zero_column.add(c)

        for r in range(MAX_ROW):
            for c in range(MAX_COLUMN):
                if r in zero_row or c in zero_column:
                    matrix[r][c] = 0

        print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().setZeroes(matrix))