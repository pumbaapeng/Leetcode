# sol 1: 1-D DP with O(n) time and space
# sol 2: if no backtracking is needed, can have O(1) space by maintaining:
#   - (#jumps, cur_reach): "by taking #jumps, I can go to anywhere within cur_reach" 
#   - "max_reach": if I have a way to get to anywhere before I did (i.e., using # jumps so far), where is the furtherist I can reach with another step"

class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        n_jumps = 0 
        cur_reach = max_reach = 0 
        for i, v in enumerate(nums) :
            max_reach = max(max_reach, i + v)
            if max_reach >= len(nums) - 1 : 
                return n_jumps + 1 
            if i == cur_reach :
                n_jumps += 1
                cur_reach = max_reach
        return -1

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    assert Solution().jump(nums) == 2
    nums = [1, 2]
    assert Solution().jump(nums) == 1
