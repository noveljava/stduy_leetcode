class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 1

        for y in range(1, m):
            for x in range(1, n):
                if y == 0 and x == 0:
                    continue
                else:
                    top = matrix[y-1][x]
                    left = matrix[y][x-1]
                    matrix[y][x] = top+left

        return matrix[m-1][n-1]

print(Solution().uniquePaths(3, 2))
