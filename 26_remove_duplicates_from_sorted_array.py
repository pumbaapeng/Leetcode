class Solution(object):
    def removeDuplicates(self, nums):
        keep, look = -1, 0
        while look < len(nums) :
            if keep == -1 or nums[keep] != nums[look] :
                keep += 1
                nums[keep] = nums[look]
            look += 1
        return keep + 1
