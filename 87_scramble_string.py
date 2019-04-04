class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        mem = {}
        return Solution.recur(s1, s2, mem)

    @staticmethod
    def recur(s1, s2, mem):
        if len(s1) != len(s2): return False
        if (s1, s2) in mem:
            return mem[(s1, s2)]
        if len(s1) == 1:
            return s1 == s2
        if s1 == s2: return True
        for i in range(1, len(s1)):
            if (Solution.recur(s1[:i], s2[:i], mem) and Solution.recur(s1[i:], s2[i:], mem)) or (Solution.recur(s1[:(len(s1) - i)], s2[i:], mem) and Solution.recur(s1[(len(s1) - i):], s2[:i], mem)):
                mem[(s1, s2)] = True
                return True
        mem[(s1, s2)] = False
        return False


if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    print(Solution().isScramble(s1, s2))