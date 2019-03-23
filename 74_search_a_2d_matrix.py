class Solution(object):
    def searchMatrix(self, matrix, target):
        """ 
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        # search in row-header: largest row-header that is <= target
        l, r = 0, nrow - 1
        bsf = -1
        while (l <= r) :
            m = (l + r) // 2
            if target >= matrix[m][0]:
                bsf = m
                l = m + 1
            else:
                r = m - 1
        if bsf == -1:
            return False
        # search in the row
        my_row = bsf
        l, r = 0, ncol - 1
        while (l <= r) :
            m = (l + r) // 2
            if target == matrix[my_row][m]:
                return True
            elif target > matrix[my_row][m]:
                l = m + 1
            else:
                r = m - 1
        return False 
