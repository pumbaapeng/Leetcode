class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] == nums[r]:
                val = nums[l]
                if val == target:
                    return True
                while (l <= r and nums[l] == val): l += 1 # NOTE: l must be allowed to cross r, otherwise won't stop (or just l += 1; no while)
                while (r >= l and nums[r] == val): r -= 1 # NOTE: r must be allowed to cross l, otherwise wor't stop (or just l += 1; no while)
                continue
            if target > nums[m]: #look for bigger
                if nums[l] <= nums[m]: #left-sorted
                    l = m + 1 
                elif nums[r] >= target:
                    l = m + 1 
                else:
                    r = m - 1 
            else: #look for smaller
                if nums[r] >= nums[m]: #right sorted
                    r = m - 1 
                elif nums[l] <= target:
                    r = m - 1 
                else:
                    l = m + 1 
        return False 
