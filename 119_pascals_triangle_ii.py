class Solution(object):                                                    
    def getRow(self, rowIndex):
        def gen_next_row(last_row):
            out = [1] 
            for l in xrange(len(last_row) - 1): 
                out.append(last_row[l] + last_row[l + 1]) 
            out.append(1)
            return out 
        last_row = []
        for row in xrange(rowIndex + 1):
            if row == 0:
                last_row = [1]
            else:
                last_row = gen_next_row(last_row)
        return last_row
