class Solution:
    def __init__(self):
        self.n_sol = 0
        
    def totalNQueens(self, n):
        if n == 0:
            return []
        self.n_sol = 0
        self.recur(0, [], n)
        ret, self.n_sol = self.n_sol, 0
        return ret

    def recur(self, idx, mem, n):
        if idx == n:
            self.n_sol += 1
            return
        candidates = self.get_candidates(mem, n)
        for cand in candidates:
            mem.append(cand)
            self.recur(idx + 1, mem, n)
            mem.pop()
        return

    def make_board(self, mem):
        n = len(mem)
        sol = []
        for c in mem:
            sol.append("." * c + 'Q' + "." * (n - c - 1))
        return sol

    def get_candidates(self, mem, n):
        ok = [True] * n
        idx = len(mem)
        sol = []
        for i, c in enumerate(mem):
            ok[c] = False
            if c - (idx - i) >= 0:
                ok[c - (idx - i)] = False
            if c + (idx - i) < n:
                ok[c + (idx - i)] = False
        for i, f in enumerate(ok):
            if f:
                sol.append(i)
        return sol
