class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        n_sign = 1 if n >= 0 else -1
        nn = abs(n)
        mul = abs(x)
        prod = 1.0
        while nn != 0:
            flag = nn & 1
            if flag == 1:
                prod *= mul
            nn >>= 1
            mul *= mul
        if x < 0 and abs(n) % 2 == 1:
            prod *= -1
        if n_sign == -1:
            prod = 1/prod
        return prod


if __name__ == '__main__':
    print(Solution().myPow(2, 3))
    print(Solution().myPow(-2, 3))
    print(Solution().myPow(2, -3))
    print(Solution().myPow(-2, -3))
