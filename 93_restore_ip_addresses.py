class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        mem = []
        Solution.recur(0, s, mem, ret)
        return ret
    
    @staticmethod
    def is_valid(s):
        if len(s) == 1:
            return True
        if s[0] == '0':
            return False
        val = int(s)
        if val >= 10 and val <= 255:
            return True
        return False
    
    @staticmethod
    def recur(idx, s, mem, ret):
        if idx == len(s) and len(mem) == 4:
            ret.append(".".join(mem))
            return
        elif len(mem) == 4:
            return
        elif idx == len(s):
            return
        if Solution.is_valid(s[idx]):
            mem.append(s[idx])
            Solution.recur(idx + 1, s, mem, ret)
            mem.pop()
        if idx + 1 < len(s) and Solution.is_valid(s[idx: idx + 2]):
            mem.append(s[idx: idx + 2])
            Solution.recur(idx + 2, s, mem, ret)
            mem.pop()
        if idx + 2 < len(s) and Solution.is_valid(s[idx: idx + 3]):
            mem.append(s[idx: idx + 3])
            Solution.recur(idx + 3, s, mem, ret)
            mem.pop()
        return
            
            
