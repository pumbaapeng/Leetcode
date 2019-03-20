class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1 
        while l <= r : 
            m = (l + r) // 2
            if nums[m] == target :
                return m
            elif nums[m] < target : # find larger
                if nums[m] > nums[l] : # left-sorted
                    l = m + 1 
                elif nums[r] < target :
                    r = m - 1 
                else :
                    l = m + 1 
            else : #find smaller
                if nums[m] < nums[r] : # right-sorted
                    r = m - 1
                elif nums[l] <= target :
                    r = m - 1 
                else :
                    l = m + 1 
        return -1   

print Solution().search([4,5,6,7,0,1,2], 0)
