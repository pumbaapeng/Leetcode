class Solution:
    def rob(self, nums: List[int]) -> int:
        max_with_last = 0
        max_without_last = 0
        for n in nums:
            max_with_last, max_without_last = n + max_without_last, max(max_with_last, max_without_last)
        return max(max_with_last, max_without_last)
