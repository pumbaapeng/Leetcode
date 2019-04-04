class Solution:
    def combine(self, n: int, k: int):
        if n == 0 or k == 0:
            return []
        ret = []
        self.recur(1, n, k, [], ret)
        return ret
    def recur(self, idx, n, k, mem, ret):
        if k == 0:
            ret.append(mem[:])
            return
        remain = n - idx + 1
        if remain < k:
            return
        mem.append(idx)
        self.recur(idx + 1, n, k-1, mem, ret)
        mem.pop()
        self.recur(idx + 1, n, k, mem, ret)
        return

if __name__ == '__main__':
    print(Solution().combine(1, 1))