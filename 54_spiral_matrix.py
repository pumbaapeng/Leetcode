class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0: return []
        ret = []
        height, width = len(matrix), len(matrix[0])
        rounds = (min(height, width) + 1 ) // 2 # trick 1
        for rnd in xrange(rounds) :
            l = t = rnd
            r = width - rnd - 1
            b = height - rnd - 1
            # top
            for col in xrange(l, r + 1):
                ret.append(matrix[t][col])
            # right
            for row in xrange(t + 1, b): # trick 2: open on both t and b
                ret.append(matrix[row][r])
            
            if b > t:                    # trick 3: skip conditionally
                for col in xrange(r, l - 1, -1):
                    ret.append(matrix[b][col])

            if l < r:
                for row in xrange(b - 1, t, -1): # open on both t and b
                    ret.append(matrix[row][l])
        return ret

ipt1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print Solution().spiralOrder(ipt1)

ipt2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print Solution().spiralOrder(ipt2)
