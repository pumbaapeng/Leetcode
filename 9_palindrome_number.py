import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x <= 9: return True
        n = int(math.log(x, 10))
        i = 0
        while i < n:
            d_i = x // math.pow(10, i) % 10
            d_n = x // math.pow(10, n) % 10
            if d_i != d_n:
                return False
            i += 1
            n -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(10))
