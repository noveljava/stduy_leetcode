from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        MAX_ROW = len(grid)
        MAX_COLUMN = len(grid[0])
        
        count = 0

        def tracking(r, c):
            check_r = [-1, 0, 1, 0]
            check_c = [0, 1, 0, -1]

            for i in range(len(check_r)):
                current_r, current_c = r+check_r[i], c+check_c[i]

                if current_r == -1 or current_c == -1:
                    continue
                    
                if current_r >= MAX_ROW or current_c >= MAX_COLUMN:
                    continue

                if grid[current_r][current_c] == "1":
                    grid[current_r][current_c] = None
                    tracking(current_r, current_c)

        for r in range(MAX_ROW):
            for c in range(MAX_COLUMN):
                if grid[r][c] == "1":
                    tracking(r, c)
                    count += 1

        return count

def bueatiful_grid_print(gird):
    print("=============")
    for r in range(len(grid)):
        for c in range(len(gird[0])):
            print(gird[r][c], " ", end="")

        print("")
    print("=============")

grid = grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))