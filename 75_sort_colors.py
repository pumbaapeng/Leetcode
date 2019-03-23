class Solution(object):
    def sortColors(self, nums):
        i_0 = cur = 0 
        i_2 = len(nums) - 1 
        while cur <= i_2:
            if nums[cur] == 1: #ignore, move cur
                cur += 1
            elif nums[cur] == 2: # swap with i_2, move i_2
                nums[cur], nums[i_2] = nums[i_2], nums[cur]
                i_2 -= 1
            else: # num[cur] == 0: swap with i_0, move both i_0 and cur
                nums[cur], nums[i_0] = nums[i_0], nums[cur]
                i_0 += 1
                cur += 1
