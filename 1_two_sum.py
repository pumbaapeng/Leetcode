class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i in xrange(len(nums)) :
            val = nums[i]
            if target - val in my_dict :
                return [my_dict[target - val], i]
            my_dict[val] = i

sol = Solution()
print sol.twoSum([2, 7, 9, 10], 9)
