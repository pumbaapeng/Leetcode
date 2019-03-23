class Solution(object):                                                                                                                                       
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        nrow = len(matrix)
        ncol = len(matrix[0])
        # header: record
        clear_col_header = False
        for col in xrange(ncol):
            if matrix[0][col] == 0:
                clear_col_header = True
                break
        clear_row_header = False
        for row in xrange(nrow):
            if matrix[row][0] == 0:
                clear_row_header = True
                break
        # non-header: record and clear
        for col in xrange(1, ncol):
            for row in xrange(1, nrow):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
        for col in xrange(1, ncol):
            if matrix[0][col] == 0:
                for row in xrange(1, nrow):
                    matrix[row][col] = 0
        for row in xrange(1, nrow):
            if matrix[row][0] == 0:
                for col in xrange(1, ncol):
                    matrix[row][col] = 0
        # header - clear
        if clear_col_header:
            for col in xrange(ncol):
                matrix[0][col] = 0 
        if clear_row_header:
            for row in xrange(nrow):
                matrix[row][0] = 0 
