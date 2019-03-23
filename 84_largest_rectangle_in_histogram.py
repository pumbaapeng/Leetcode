class Solution(object):
    def largestRectangleArea(self, heights):
        mem = []
        max_area = 0;
        heights.append(0);
        for r, v in enumerate(heights):
            while len(mem) > 0 and mem[-1][1] > v : 
                i, h = mem.pop()
                l = mem[-1][0] if len(mem) > 0 else -1
                area = (r - l - 1) * h 
                max_area = max(area, max_area)
            mem.append((r, v)) # NOTE: do not do it conditionally because the left-wall would be inaccurate     
        return max_area 
