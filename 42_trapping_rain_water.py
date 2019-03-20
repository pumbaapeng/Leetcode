# Key observations :
#   1) water level with go monotonically up then down
#      - this hints at a (sub-optimal) solution for finding the maximal point first, then do this in two pass
#   2) if we start from both ends, then the lower side always has the accurate water level
#      - this is because the pairing wall for the lower side will be at least as high as the higher side
#      - this hints at a one-pass (optimal) solution for squeezing from two sides to the middle, until the two boundaries touch
#   
class Solution(object):
    def trap(self, height):
        water_total = 0
        l, r = 0, len(height) - 1
        wlevel_l, wlevel_r = -1, -1
        while l < r :
            hl, hr = height[l], height[r]
            if hl < hr:
                wlevel_l = max(wlevel_l, hl)
                water_total += (wlevel_l - hl)
                l += 1
            else:
                wlevel_r = max(wlevel_r, hr)
                water_total += (wlevel_r - hr)
                r -= 1
        return water_total

