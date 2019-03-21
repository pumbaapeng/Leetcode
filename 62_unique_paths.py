class Solution(object):
    def uniquePaths(self, m, n):
        if m == 0 or n == 0 :
            return 1
        nrow = min(m, n)
        ncol = max(m, n)
        mem = [0 for i in xrange(ncol + 1)]
        mem[1] = 1
        for row in xrange(nrow):
            for col in xrange(ncol):
                j_idx = col + 1
                mem[j_idx] = mem[j_idx] + mem[j_idx - 1]
        return mem[ncol]

print Solution().uniquePaths(7, 3)
