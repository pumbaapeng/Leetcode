class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        mem = set()
        return Solution.recur(0,0,0, s1, s2, s3, mem)
    
    @staticmethod
    def recur(i1, i2, i3, s1, s2, s3, mem):
        if (i1, i2, i3) in mem:
            return False
        if i3 == len(s3): #this implies that all i1, i2, i3 are used up
            return True
        if i1 < len(s1) and s1[i1] == s3[i3]:
            if Solution.recur(i1 + 1, i2, i3 + 1, s1, s2, s3, mem):
                return True
        if i2 < len(s2) and s2[i2] == s3[i3]:
            if Solution.recur(i1, i2 + 1, i3 + 1, s1, s2, s3, mem):
                return True
        mem.add((i1, i2, i3))
        return False
