#  Idea: Moore's majority vote algorithm
#         cancel out different elements, and only the majority can stand at the end
#         note that non-majority elements can be canceled, too, but that would just make majority even more "major", such that the ma
#  
#   O(n) time and O(1) space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        assert(len(nums) > 0)
        majority = None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                majority = nums[i]
                count = 1
            else:
                count += (1 if nums[i] == majority else -1)
        return majority
