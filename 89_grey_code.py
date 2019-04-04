# trick: mirroring
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ret = [0, 1]
        for i in range(2, n + 1):
            ret_rev = ret[::-1]
            ret_rev = [v | (1 << (i - 1)) for v in ret_rev]
            ret += ret_rev
        return ret
