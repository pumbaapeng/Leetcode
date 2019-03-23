class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def gen_next_row(last_row):
            out = [1]
            for l in xrange(len(last_row) - 1):
                out.append(last_row[l] + last_row[l + 1])
            out.append(1)
            return out
        ret = []
        for row in xrange(numRows):
            if row == 0:
                ret.append([1])
            else:
                ret.append(gen_next_row(ret[-1]))
        return ret
