class Solution:
    def solveNQueens(self, n):
        if n == 0:
            return []
        ret = []
        self.recur(0, [], ret, n)
        return ret

    def recur(self, idx, mem, ret, n):
        if idx == n:
            ret.append(self.make_board(mem))
            return
        candidates = self.get_candidates(mem, n)
        for cand in candidates:
            mem.append(cand)
            self.recur(idx + 1, mem, ret, n)
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
