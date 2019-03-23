class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recur(nums, idx, mem, ret):
            if idx == len(nums):
                ret.append(mem[:])
                return
            recur(nums, idx + 1, mem, ret)
            mem.append(nums[idx])
            recur(nums, idx + 1, mem, ret)
            mem.pop()
        ret = []
        recur(nums, 0, [], ret)
        return ret
