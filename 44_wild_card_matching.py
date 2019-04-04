class Solution:
    @staticmethod
    def recur(ls, lp, s, p, mem):
        if ls == len(s) and lp == len(p):
            return True
        if (ls, lp) in mem:
            return False
        if ls == len(s):
            while lp < len(p):
                if p[lp] != '*':
                    mem.add((ls, lp))
                    return False
                lp += 1
            return True
        if ls == len(s) or lp == len(p):
            mem.add((ls, lp))
            return False
        if p[lp] != '?' and p[lp] != '*':
            if s[ls] == p[lp]:
                return Solution.recur(ls + 1, lp + 1, s, p, mem)
            mem.add((ls, lp))
            return False
        if p[lp] == '?':
            return Solution.recur(ls + 1, lp + 1, s, p, mem)
        # p[ls] == '*'
        new_lp = lp + 1
        while new_lp < len(p) and p[new_lp] == '*':
            new_lp += 1
        for new_ls in range(ls, len(s) + 1):
            if Solution.recur(new_ls, new_lp, s, p, mem):
                return True
            else:
                mem.add((new_ls, new_lp))
        mem.add((ls, lp))
        return False

    def isMatch(self, s: str, p: str) -> bool:
        mem = set()
        return Solution.recur(0, 0, s, p, mem)


if __name__ == '__main__':
    s = "acdcb"
    p = "a*c?b"
    print(Solution().isMatch(s, p))


