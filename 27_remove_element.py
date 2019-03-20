class Solution(object):
    def removeElement(self, nums, val):
        keep, look = -1, 0
        while look < len(nums) :
            if nums[look] != val :
                keep += 1
                nums[keep] = nums[look]
            look += 1
        return keep + 1
