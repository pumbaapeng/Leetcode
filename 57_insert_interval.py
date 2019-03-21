# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        ret =  []
        inserted = False
        for inv in intervals:
            if not inserted:
                if inv.end < newInterval.start:
                    ret.append(inv)
                else :
                    inserted = True
                    if inv.start > newInterval.end:
                        ret.append(newInterval)
                        ret.append(inv)
                    else:
                        newInterval.start, newInterval.end = min(newInterval.start, inv.start), max(newInterval.end, inv.end)
                        ret.append(newInterval)
            else:
                    if inv.start > newInterval.end:
                        ret.append(inv)
                    else:
                        ret[-1].end = max(ret[-1].end, inv.end)
        if not inserted:
            ret.append(newInterval)
        return ret

if __name__ == "__main__":
    intervals = [Interval(1, 3), Interval(6, 9)]
    newInterval = Interval(2, 5)
    assert Solution().insert(intervals,
                             newInterval) == [Interval(1, 5), Interval(6, 9)]
    intervals = [
        Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10),
        Interval(12, 16)
    ]
    newInterval = Interval(4, 9)
    assert Solution().insert(intervals, newInterval) == [
        Interval(1, 2), Interval(3, 10), Interval(12, 16)
    ]
