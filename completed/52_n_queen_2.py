import copy

class Solution:
    def backtracking(self, row, n, chess_board, result):
        if row == n:
            info: list = []
            for row in chess_board:
                info.append(''.join(row))
            
            result.append(info)
            return

        for i in range(n):
            chess_board_copy = copy.deepcopy(chess_board)
            is_ok = True
            for find_position in range(1, row+1):
                if chess_board_copy[row-find_position][i] == "Q":
                    is_ok = False
                elif i-find_position >= 0 and chess_board_copy[row-find_position][i-find_position] == "Q":
                    is_ok = False
                elif i+find_position < n and chess_board_copy[row-find_position][i+find_position] == "Q":
                    is_ok = False

            if is_ok:
                chess_board_copy[row][i] = "Q"
                self.backtracking(row+1, n, chess_board_copy, result)
            

    def totalNQueens(self, n: int) -> int:
        chess_board = [['.' for _ in range(n)] for _ in range(n)]
        result: list = []

        for i in range(0, n):
            chess_board_copy = copy.deepcopy(chess_board)
            chess_board_copy[0][i] = "Q"
            self.backtracking(1, n, chess_board_copy, result)

        return len(result)        