# Nice exercise in fine-grained control of recursive program optiomization
class Solution(object):
    def combinationSum2(self, candidates, target):
        def recur(candidates, idx, buf, ret, target) :
            if target < 0:
                return
            if target == 0:
                ret.append(buf[:])
                return
            if idx >= len(candidates) :
                return
            candid = candidates[idx]
            max_count = 1 
            while idx + max_count < len(candidates) and candidates[idx + max_count] == candid : max_count += 1
            nxt_idx = idx + max_count
            max_count = min(max_count, target // candid)
            for count in xrange(max_count + 1) :
                if count != 0: buf.append(candid)
                recur(candidates, nxt_idx, buf, ret, target - candid * count)
            for count in xrange(max_count) : buf.pop()
        candidates.sort()
        ret = []
        recur(candidates, 0, [], ret, target)
        return ret

if __name__ == "__main__":
    print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]][::-1]

