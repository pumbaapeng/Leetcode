class Solution(object):
    def singleNumber(self, nums):
        ret = 0
        for n in nums:
            ret ^= n
        return ret
