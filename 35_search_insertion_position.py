class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        bsf = len(nums)
        while (l <= r) :
            m = (l + r) // 2
            if nums[m] >= target:
                bsf = m
                r = m - 1
            else:
                l = m + 1
        return bsf
