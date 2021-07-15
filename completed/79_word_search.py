from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROW = len(board)
        MAX_COLUMN = len(board[0])

        def isValid(r, c, word):
            if len(word) == 0:
                return True

            min_column = max(0, c-1)
            max_column = min(MAX_COLUMN-1, c+1)

            min_row = max(0, r-1)
            max_row = min(MAX_ROW-1, r+1)

            row_info = [r, r, min_row, max_row]
            column_info = [min_column, max_column, c, c]

            current_word = board[r][c]
            board[r][c] = None

            for i in range(4):
                check_row, check_column = row_info[i], column_info[i]
                if board[check_row][check_column] == word[0]:
                    if isValid(check_row, check_column, word[1:]):
                        return True

            board[r][c] = current_word

            return False

        for r in range(MAX_ROW):
            for c in range(MAX_COLUMN):
                if board[r][c] == word[0]:
                    # findfirst index
                    if isValid(r, c, word[1:]):
                        return True

        return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

print(Solution().exist(board, word))