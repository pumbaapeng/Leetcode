class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ret = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                inner_target = target - (nums[i] + nums[j])
                k, l = j + 1, len(nums) - 1
                while k < l :
                    cur_sum = nums[k] + nums[l]
                    if cur_sum == inner_target :
                        print "inner_target = %d, cur_sum = %d" % (inner_target, cur_sum)
                        ret.append([nums[i], nums[j], nums[k], nums[l]])
                        k, l = k + 1, l - 1
                        while k < l and nums[k] == nums[k-1] : k += 1
                        while k < l and nums[l] == nums[l+1] : l -= 1
                    elif cur_sum > inner_target :
                        l -= 1
                    else :
                        k += 1
                j += 1
                while j < len(nums) - 2 and nums[j] == nums[j - 1]: j+= 1
            i += 1
            while i < len(nums) - 3 and nums[i] == nums[i - 1]: i += 1
        return ret

if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    assert Solution().fourSum(nums, 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2],[-1, 0, 0, 1]]
    nums = [0,0,0,0]
    print Solution().fourSum(nums, 1)
