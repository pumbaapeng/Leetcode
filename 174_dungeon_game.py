# Key idea: 2D-DP
# - memory: the least amount of HP when entering this cell given a feasible game
# - filling-order: reverse
# - recursion: max-min logic
# - initial condition: relatively sophisticated

# O(mn) memory version: more easily understood
# O(n)-memory version applies
class Solution:
    def calculateMinimumHP(self, maze):
        if len(maze) == 0 or len(maze[0]) == 0:
            return 0
        nrow, ncol = len(maze), len(maze[0])
        ans = [[float('inf') for c in range(ncol + 1)] for r in range(nrow + 1)]
        ans[nrow - 1][ncol] = 1
        for r in range(nrow - 1, -1, -1):
            for c in range(ncol - 1, -1, -1):
                cur_ans = min(ans[r + 1][c], ans[r][c + 1]) - maze[r][c]  # pick an easier path forward
                cur_ans = max(cur_ans, 1)  # need to be alive when entering this cell
                ans[r][c] = cur_ans
        return ans[0][0]

if __name__ == '__main__':
    maze = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP(maze))