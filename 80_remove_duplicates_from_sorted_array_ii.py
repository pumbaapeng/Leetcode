class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ins = cnt = 0
        prev = None
        for val in nums:
            if val == prev:
                cnt += 1
            else:
                cnt = 1
            if cnt < 3:
                nums[ins] = val
                ins += 1
            prev = val
        return ins
