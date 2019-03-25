# Note: python integer has 24 ~ 36 bytes, so for this questions overflow was defined as anything outside of [-2^32, 2^31 - 1]

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        int_max = (1 << 31) - 1
        int_min = (1 << 31) * -1
        sign = 1 if x >= 0 else -1
        x = abs(x)
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        sum = 0
        for d in digits:
            sum = sum * 10 + d
        sum *= sign
        if sum > int_max or sum < int_min:
            return 0
        else:
            return sum
