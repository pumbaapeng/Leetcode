# NOTE: this problem is a great DP question because special care needs be take for (2) and (3) below for a O(n) memory solution
# DP-keys:
# 1) recursion
# 2) boundary condition
# 3) filling a

class Solution(object):
    def minimumTotal(self, triangle):
        sol = [float('inf') for i in xrange(len(triangle) + 1)]
        sol[1] = 0
        for row in triangle:
            for i,v in reversed(list(enumerate(row))): # NOTE: this line is memory hungry because list converts the iterator. needs to write more code to iterate both idx and val from the end
                sol[i+1] = min(sol[i], sol[i+1]) + v
        return min(sol)


ipt = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print Solution().minimumTotal(ipt)
