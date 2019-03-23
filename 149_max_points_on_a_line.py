# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        max_ret = 2
        for i, center in enumerate(points[0:(len(points) - 1)]):
            counts, dup_centers = {}, 0
            for j, end in enumerate(points[(i + 1): len(points)]):
                if center.x == end.x and center.y == end.y:
                    dup_centers += 1
                    continue
                slope = float(center.y - end.y) / float(center.x - end.x) if center.x - end.x != 0 else float('inf')
                counts[slope] = counts[slope] + 1 if slope in counts else 2
            max_ret = max(dup_centers + 1, max_ret)
            for s, c in counts.iteritems():
                max_ret = max(c + dup_centers, max_ret)
        return max_ret
