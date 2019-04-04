# Start: 3:39
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return
        nrow = len(board)
        ncol = len(board[0])
        for r in range(nrow):
            self.dfs_paint_y(r, 0, board)
            self.dfs_paint_y(r, ncol - 1, board)
        for c in range(ncol):
            self.dfs_paint_y(0, c, board)
            self.dfs_paint_y(nrow - 1, c, board)
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 'Y':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return

    def dfs_paint_y(self, r, c, board):
        nrow, ncol = len(board), len(board[0])
        if r < 0 or r >= nrow or c < 0 or c >= ncol:
            return
        if board[r][c] == 'X' or board[r][c] == 'Y':
            return
        board[r][c] = 'Y'
        self.dfs_paint_y(r - 1, c, board)
        self.dfs_paint_y(r + 1, c, board)
        self.dfs_paint_y(r, c - 1, board)
        self.dfs_paint_y(r, c + 1, board)
        return