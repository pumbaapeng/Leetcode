class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = 1
        prev_min = 1
        sol = float('-inf')
        for num in nums:
            cur_max = max(num, num * prev_max, num * prev_min)
            cur_min = min(num, num * prev_max, num * prev_min)
            sol = max(sol, cur_max)
            prev_max, prev_min = cur_max, cur_min
        return sol
