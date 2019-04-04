class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.recur(nums, set(), [], ret)
        return ret
    def recur(self, nums, used, mem, ret):
        if len(mem) == len(nums):
            ret.append(mem[:])
            return
        for num in nums:
            if num in used:
                continue
            mem.append(num)
            used.add(num)
            self.recur(nums, used, mem, ret)
            mem.pop()
            used.remove(num)
        return
