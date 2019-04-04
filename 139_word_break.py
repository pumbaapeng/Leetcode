class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False for i in range(len(s))]
        for r in range(1, len(s) + 1):
            for l in range(r):
                if s[l:r] in wordDict and (l == 0 or ans[l - 1]):
                    ans[r - 1] = True
                    break
        return ans[-1]
