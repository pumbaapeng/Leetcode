from functools import reduce


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        mem = [v + 1 for v in range(n)]
        factorial = reduce(lambda x, y: x * y, mem)
        ret = ""
        k = k - 1 # make it 0-based
        for i in range(n):
            factorial //= (n - i)
            rank = k // factorial
            k %= factorial
            ret += str(mem[rank])
            del mem[rank]
        return ret


if __name__ == '__main__':
    print(Solution().getPermutation(4, 9)) # "2341"
