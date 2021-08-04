from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything,  modify matrix in-place instead.
        """
        replaced_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # 계산식에 의해서 바뀔 장소를 찾는다. 그리고 새로운 메모리에 바꿀 데이터를 채워둔다
                replaced_i = j
                replaced_j = len(matrix) - 1 - i
                replaced_matrix[replaced_i][replaced_j] = matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = replaced_matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    assert [[7, 4, 1], [8, 5, 2], [9, 6, 3]] == matrix

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    Solution().rotate(matrix)

    assert [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] == matrix
