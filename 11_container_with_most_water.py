class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r :
            cur_water = min(height[l], height[r]) * (r - l)
            max_water = max(max_water, cur_water)
            if height[l] < height[r] :
                l += 1
            else :
                r -= 1
        return max_water

if __name__ == "__main__":
    height = [1, 3, 2]
    assert Solution().maxArea(height) == 2
    height = [1, 1]
    assert Solution().maxArea(height) == 1
    height = [1, 2, 1]
    assert Solution().maxArea(height) == 2
