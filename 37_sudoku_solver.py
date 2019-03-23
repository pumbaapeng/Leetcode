class Solution(object):                   
    def solveSudoku(self, board):
        col_choices = Solution.init_col_choices(board)
        row_choices = Solution.init_row_choices(board)
        block_choices = Solution.init_block_choices(board)
        Solution.recur(0, col_choices, row_choices, block_choices, board)
    
    @classmethod
    def recur(cls, idx, col_choices, row_choices, block_choices, board):
        if idx == 81:
            return True
        row, col = idx // 9, idx % 9
        if board[row][col] != ".": 
            return Solution.recur(idx + 1, col_choices, row_choices, block_choices, board) # NOTE: forgot the add "return" here, resulted in a costly bug
        i_block, j_block = row // 3, col // 3
        valid_choices = row_choices[row] & col_choices[col] & block_choices[i_block][j_block]
        # for all valid choice, try it and recur
        for item in valid_choices:
            row_choices[row].remove(item)
            col_choices[col].remove(item)
            block_choices[i_block][j_block].remove(item)
            board[row][col] = item
            if Solution.recur(idx + 1, col_choices, row_choices, block_choices, board):
                return True
            board[row][col] = "."
            block_choices[i_block][j_block].add(item)
            col_choices[col].add(item)
            row_choices[row].add(item)
        return False
    
    @classmethod
    def init_row_choices(cls, board):
        ret = []
        for row in xrange(9):
            choices = {"%d" % num for num in xrange(1,10)}
            for col in xrange(9):
                item = board[row][col]
                if item != ".":
                    choices.remove(item)
            ret.append(choices)
        return ret
    
    @classmethod
    def init_col_choices(cls, board):
        ret = []
        for col in xrange(9):
            choices = {"%d" % num for num in xrange(1,10)}
            for row in xrange(9):
                item = board[row][col]
                if item != ".":
                    choices.remove(item)
            ret.append(choices)
        return ret
    
    @classmethod
    def init_block_choices(cls, board):
        ret = []
        for block_i in xrange(3):
            ret_i = []
            for block_j in xrange(3):
                choices = {"%d" % num for num in xrange(1,10)}
                for i in xrange(3):
                    for j in xrange(3):
                        row = block_i * 3 + i
                        col = block_j * 3 + j
                        item = board[row][col]
                        if item != ".":
                            choices.remove(item)
                ret_i.append(choices)
            ret.append(ret_i)
        return ret

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print board
