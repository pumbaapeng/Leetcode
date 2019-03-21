import pprint
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        ret = []
        intervals.sort(key = lambda itv: itv.start)
        for interval in intervals:
            if len(ret) == 0 or ret[-1].end < interval.start:
                ret.append(interval)
            else:
                ret[-1].end = max(interval.end, ret[-1].end)
        return ret

## NOTE: for unknow reason, this doesn't run (despite it passes on LeetCode) ##

if __name__ == "__main__":
    intervals = [
        Interval(1, 3),
        Interval(2, 6),
        Interval(8, 10),
        Interval(15, 18)
    ]
    pp = pprint.PrettyPrinter(depth = 5)
    pp.pprint(Solution().merge(intervals))
    assert Solution().merge(intervals) == [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
    intervals = [Interval(1, 4), Interval(2, 5)]
    assert Solution().merge(intervals) == [Interval(1, 5)]

