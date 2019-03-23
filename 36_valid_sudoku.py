class Solution(object):
    def isValidSudoku(self, board):
        #row
        for row in xrange(9):
            mem = set()
            for col in xrange(9):
                cell = board[row][col]
                if cell == ".": continue
                if cell in mem: return False
                mem.add(cell)
        #col
        for col in xrange(9):
            mem = set()
            for row in xrange(9):
                cell = board[row][col]
                if cell == ".": continue
                if cell in mem: return False
                mem.add(cell)
        #block
        for block_i in xrange(3):
            for block_j in xrange(3):
                mem = set()
                for i in xrange(3):
                    for j in xrange(3):
                        row = block_i * 3 + i
                        col = block_j * 3 + j
                        cell = board[row][col]
                        if cell == ".": continue
                        if cell in mem: return False
                        mem.add(cell)
        return True
