class Solution(object):
    def generateMatrix(self, n):
        ret = [[-1 for i in xrange(n)] for j in xrange(n)]
        rounds = (n + 1) // 2
        num = 1
        for rnd in xrange(rounds) :
            l = t = rnd
            r = b = n - rnd - 1
            for col in xrange(l, r + 1):
                ret[t][col] = num
                num += 1
            for row in xrange(t + 1, b): # trick 2: open on both t and b
                matrix[row][r] = num
                num += 1
            if b > t:                    # trick 3: skip conditionally
                for col in xrange(r, l - 1, -1):
                    matrix[b][col] = num
                    num += 1
            if l < r:
                for row in xrange(b - 1, t, -1): # open on both t and b
                    matrix[row][l] = num
                    num += 1
        return ret
