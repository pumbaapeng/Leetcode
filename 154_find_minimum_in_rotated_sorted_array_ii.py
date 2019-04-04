class Solution:
    def findMin(self, nums) -> int:
        assert (len(nums) > 0)
        ret = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == nums[r]:
                val = nums[l]
                ret = min(val, ret)
                while l <= r and nums[l] == val:
                    l += 1
                while l <= r and nums[r] == val:
                    r -= 1
                continue
            m = (l + r) // 2
            val = nums[m]
            ret = min(val, ret)
            if val <= nums[r]:
                r = m - 1
            else:
                l = m + 1
        return ret


if __name__ == '__main__':
    print(Solution().findMin([2,0,1,1,1]))
