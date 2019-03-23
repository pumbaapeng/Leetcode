class Solution(object):
    def minWindow(self, s, t):
        req = {}
        for c in t:
            if c in req : req[c] += 1
            else: req[c] = 1
        found = {k:0 for k in req}
        matched = 0
        min_len = float('inf')
        ret = ""
        l = 0
        for r,c in enumerate(s) :
            if c in req:
                found[c] += 1
                if found[c] == req[c]:
                    matched += 1
            if matched == len(req):
                while l < r and (s[l] not in req or found[s[l]] > req[s[l]]):
                    if s[l] in req:
                        found[s[l]] -= 1
                    l += 1
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ret = s[l:(r + 1)]
        return ret

s = "aa"
t = "aa"
print Solution().minWindow(s, t)
