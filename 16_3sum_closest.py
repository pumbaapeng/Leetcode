class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        ret = sum(nums[0:3])
        i = 0 
        while i < len(nums) - 2 :
            j, k = i + 1, len(nums) - 1
            while j < k :
                cur_sum = nums[i] + nums[j] + nums[k]
                if abs(ret - target) > abs(cur_sum - target) :
                    ret = cur_sum
                if cur_sum == target:
                    return target
                elif cur_sum > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        return ret

if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    print Solution().threeSumClosest(nums, 1)
    assert Solution().threeSumClosest(nums, 1) == 2
