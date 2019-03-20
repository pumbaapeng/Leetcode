class Solution(object):
    def nextPermutation(self, nums):
        # find the first decrease, call it the pivot
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1] :
            pivot -= 1
        if pivot == -1 :
            nums[:] = nums[::-1] ## NOTE: for nested objects, python make a copy of its address. if the address is changed it would be ok (but not affecting the output)
            return
        # in the RHS, find the smallest guy that is larger than the pivot
        j = len(nums) - 1
        while j > pivot and nums[j] <= nums[pivot] :
            j -= 1
        # swap the pivot with the guy, then reverse the RHS
        nums[pivot], nums[j] = nums[j], nums[pivot] 
        nums[pivot + 1:] = nums[pivot + 1:][::-1]

if __name__ == "__main__":
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    assert nums == [1, 3, 2]
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print nums
    assert nums == [1, 2, 3]
    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    assert nums == [1, 5, 1]
    nums = [1, 5, 1]
    Solution().nextPermutation(nums)
    assert nums == [5, 1, 1]
    nums = [5, 1, 1]
    Solution().nextPermutation(nums)
    assert nums == [1, 1, 5]

