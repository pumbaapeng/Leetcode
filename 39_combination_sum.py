class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates.sort()
        def recur(candidates, idx, buf, target, ret):
            if idx == len(candidates): # NOTE: always return in terminal condition, regardless of write to an output or not
                if target == 0:
                    ret.append(buf[:]) # NOTE: make a copy!
                return
            candid = candidates[idx]
            for count in xrange(target // candid + 1) :
                if count != 0: buf.append(candid)
                recur(candidates, idx + 1, buf, target - count * candid, ret)
            for count in xrange(target // candid):
                buf.pop()
            
        recur(candidates, 0, [], target, ret)
        return ret
        
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    print Solution().combinationSum(candidates, 7)
    assert Solution().combinationSum(candidates, 7) == [[7], [2, 2, 3]]
