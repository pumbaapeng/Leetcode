class Solution(object):
    def subsetsWithDup(self, nums):
        def recur(idx, nums, mem, ret):
            if idx >= len(nums):
                ret.append(mem[:])
                return
            nxt_idx = idx + 1
            while nxt_idx < len(nums) and nums[nxt_idx] == nums[idx]: nxt_idx += 1
            max_cnt = nxt_idx - idx
            for cnt in xrange(max_cnt + 1):
                if cnt != 0:
                    mem.append(nums[idx])
                recur(nxt_idx, nums, mem, ret)
            for cnt in xrange(max_cnt):
                mem.pop()
        nums.sort()
        ret = []
        recur(0, nums, [], ret)
        return ret
