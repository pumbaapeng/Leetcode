class Solution(object):
    def minPathSum(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0: # NOTE: notice corner case
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        mem = [float('inf') for j in xrange(ncol + 1)] # NOTE: notice initial condition
        mem[1] = 0
        for row in xrange(nrow):
            for col in xrange(ncol):
                mem[col + 1] = min(mem[col], mem[col+1]) + grid[row][col]
        return mem[ncol]
        
ipt = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print Solution().minPathSum(ipt)
