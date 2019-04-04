class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = [False for i in range(len(s))]
        preds = [[] for i in range(len(s))]
        for r in range(1, len(s) + 1):
            for l in range(r):
                if s[l:r] in wordDict and (l == 0 or ans[l - 1]):
                    ans[r - 1] = True
                    preds[r - 1].append(l - 1)
        ret = []
        self.dfs(len(s) - 1, s, [], ret, preds)
        return ret

    def dfs(self, end_idx, s, mem, ret, preds):
        if end_idx < 0:
            ret.append(" ".join(reversed(mem)))
            return
        for pred in preds[end_idx]:
            beg_idx = pred + 1
            word = s[beg_idx:(end_idx + 1)]
            mem.append(word)
            self.dfs(pred, s, mem, ret, preds)
            mem.pop()
        return
