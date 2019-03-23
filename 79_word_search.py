class Solution(object):
    def exist(self, board, word):
        def dfs(board, used, word, idx, i, j):
            if idx == len(word): return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[idx] != board[i][j] or (i,j) in used: return False
            used.add((i,j))
            if dfs(board, used, word, idx + 1, i+1, j): return True
            if dfs(board, used, word, idx + 1, i-1, j): return True
            if dfs(board, used, word, idx + 1, i, j+1): return True
            if dfs(board, used, word, idx + 1, i, j-1): return True
            used.remove((i,j))
            return False
        if len(board) == 0 or len(board[0]) == 0: return False
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if dfs(board, set(), word, 0, row, col): return True
        return False


ipt = [["a","b"]]
print Solution().exist(ipt, "ba")
