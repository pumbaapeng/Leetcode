# O(n^2) time and complexity
class Solution:
    def minCut(self, s: str) -> int:
        ans = [0 for i in range(len(s) + 1)]
        palin = self.build_palin_table(s)
        for r in range(1, len(s) + 1):
            min_chunk = ans[r - 1] + 1
            for l in range(1, r):
                if palin[l - 1][r - 1]:
                    cur_chunk = ans[l - 1] + 1
                    min_chunk = min(cur_chunk, min_chunk)
            ans[r] = min_chunk
        return ans[-1] - 1
    
    def build_palin_table(self, s):
        ret = [[False for j in range(len(s))] for i in range(len(s))]
        for c in range(len(s)):
            for j in range(min(c + 1, len(s) - c)):
                if s[c - j] == s[c + j]:
                    ret[c - j][c + j] = True
                else:
                    break
        for cr in range(len(s)):
            dl, dr = 1, 0
            while cr - dl >= 0 and cr + dr < len(s):
                if s[cr - dl] == s[cr + dr]:
                    ret[cr - dl][cr + dr] = True
                else:
                    break
                dr += 1
                dl += 1
        return ret
                
    def is_palin(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
