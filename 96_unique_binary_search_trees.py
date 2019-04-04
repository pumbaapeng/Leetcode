# key: the new node need to be connected from top-left and bottom-left; one has ans[j] options and the other has ans[i - 1 - j] options
class Solution:
    def numTrees(self, n: int) -> int:
        ans = [1 for i in range(n + 1)]
        for i in range(2, n + 1):
            tot = 0
            for j in range(i):
                tot += ans[j] * ans[i - 1 - j]
            ans[i] = tot
        return ans[n]
