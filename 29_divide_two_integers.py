class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)
        negative = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        tmp_b = b
        tmp_q = 1
        while tmp_b <= a:
            tmp_b <<= 1
            tmp_q <<= 1
        # accumulate q in a binary way
        q = 0
        while tmp_q != 0:
            if tmp_b <= a:
                a -= tmp_b
                q += tmp_q
            tmp_b >>= 1
            tmp_q >>= 1
        if negative:
            q = -q
        
        if q < -(1<<31) or q > ((1 << 31) - 1):
            q = (1 << 31) - 1
        return q
