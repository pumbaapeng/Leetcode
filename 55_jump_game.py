class Solution(object):
    def canJump(self, nums):
        mr = 0 # max_reach
        for i,v in enumerate(nums):
            if mr < i:
                return False
            mr = max(mr, i + nums[i])
            if mr >= len(nums) - 1:
                return True
