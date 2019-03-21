class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for rnd in range(n // 2) :
            l = u = rnd
            r = d = n - 1 - rnd
            passes = n - 2 * rnd - 1
            for j in xrange(passes) :
                matrix[u][rnd + j], matrix[rnd + j][r], matrix[d][n - 1 - rnd - j], matrix[n - 1 - rnd - j][l] =  matrix[n - 1 - rnd - j][l], matrix[u][rnd + j], matrix[rnd + j][r], matrix[d][n - 1 - rnd - j]

            
