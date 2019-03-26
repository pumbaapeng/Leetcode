import math

class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum = 0
        while n > 0:
            sum += (n // 5)
            n //= 5
        return sum

if __name__ == '__main__':
    print(Solution().trailingZeroes(200))