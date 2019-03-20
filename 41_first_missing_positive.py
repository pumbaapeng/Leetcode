class Solution(object):
    def firstMissingPositive(self, nums):
        buf = -1
        for i, val in enumerate(nums):
            if val == i + 1:
                continue
            else:
                nums[i] = -1
                buf = val
                while buf >= 1 and buf <= len(nums) and nums[buf - 1] != buf:
                    # buf, nums[buf - 1] = nums[buf - 1], buf #NOTE: this doesn't work! python swapping involving arrange indices is not functioning correctly. use explicit swapping instead
                    tmp = buf
                    buf = nums[tmp - 1]
                    nums[tmp-1] = tmp
        for i,val in enumerate(nums):
            if val == -1:
                return i + 1
        return len(nums) + 1
        
if __name__ == "__main__":
    nums = [1, 2, 0]
    assert Solution().firstMissingPositive(nums) == 3
    nums = [3, 4, -1, 1]
    assert Solution().firstMissingPositive(nums) == 2
    nums = []
    assert Solution().firstMissingPositive(nums) == 1

