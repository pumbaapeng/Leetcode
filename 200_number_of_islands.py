class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        ret = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == '1':
                    ret += 1
                    self.paint_dfs(i, j, grid)
        return ret
    
    def paint_dfs(self, r, c, grid):
        nrow = len(grid)
        ncol = len(grid[0])
        if r < 0 or r >= nrow or c < 0 or c >= ncol or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.paint_dfs(r+1, c, grid)
        self.paint_dfs(r-1, c, grid)
        self.paint_dfs(r, c+1, grid)
        self.paint_dfs(r, c-1, grid)
        return
