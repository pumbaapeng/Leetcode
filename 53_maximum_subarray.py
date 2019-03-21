class Solution(object):
    def maxSubArray(self, nums):
        cum_sum = 0
        min_cum_sum = 0
        max_sub_sum = float('-inf')
        for i,v in enumerate(nums) : 
            cum_sum += v
            max_sub_sum = max(cum_sum - min_cum_sum, max_sub_sum)
            min_cum_sum = min(cum_sum, min_cum_sum)
        return max_sub_sum

if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([-1]) == -1

