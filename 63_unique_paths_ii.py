class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        nrow = len(obstacleGrid)
        if nrow == 0: return 0
        ncol = len(obstacleGrid[0])
        if ncol == 0: return 0
        mem = [0 for i in xrange(ncol + 1)]
        mem[1] = 1
        for row in xrange(nrow):
            for col in xrange(ncol):
                j = col + 1
                up_mul = 1 if row - 1 < 0 or obstacleGrid[row - 1][col] == 0 else 0
                left_mul = 1 if col - 1 < 0 or obstacleGrid[row][col - 1] == 0 else 0
                cur_mul = 1 if obstacleGrid[row][col] == 0 else 0
                mem[j] = cur_mul * (mem[j] * up_mul + mem[j-1] * left_mul)
        return mem[ncol]
