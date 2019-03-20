class Solution(object):
    def searchRange(self, nums, target):
        """ 
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_elem_LE_target(nums, target):
            l, r = 0, len(nums) - 1 
            bsf = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else :
                    bsf = m
                    r = m - 1
            return bsf
        idx = first_elem_LE_target(nums, target)
        if idx == -1 or nums[idx] != target :
            return [-1, -1]
        left = idx
        while idx + 1 < len(nums) and nums[idx + 1] == target : idx += 1
        return [left, idx]    
