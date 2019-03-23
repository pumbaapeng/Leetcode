class Solution(object):
    def findRepeatedDnaSequences(self, s):
        ret = []
        occur = {}
        for i in xrange(0, len(s) - 10 + 1):
            str = s[i:min((i + 10), len(s))]
            occur[str] = 1 if str not in occur else occur[str] + 1
        for k, v in occur.iteritems():
            if v >= 2:
                ret.append(k)
        return ret


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print Solution().findRepeatedDnaSequences(s)
