class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            v = nums[m]
            if (m - 1 <= -1 or nums[m - 1] < v) and (m + 1 >= len(nums) or nums[m + 1] < v):
                return m
            if (m + 1 < len(nums) and nums[m + 1] > v):
                l = m + 1
            else:
                r = m - 1