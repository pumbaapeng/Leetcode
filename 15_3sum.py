class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            target = nums[i] * -1
            while j < k :
                cur_sum = nums[j] + nums[k]
                if cur_sum == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    while k > j and nums[k] == nums[k + 1]: k -= 1
                elif cur_sum < target:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i - 1] == nums[i]: i += 1
        return res

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    assert Solution().threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
    nums = [-2, 0, 1, 1, 2]
    assert Solution().threeSum(nums) == [[-2, 0, 2], [-2, 1, 1]]
