class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """ 
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        positive = numerator * denominator >= 0
        numerator, denominator = abs(numerator), abs(denominator)
        int_q = numerator // denominator
        r = numerator % denominator
        qr_map = {}
        digits = []
        rep_digit = -1
        while r : 
            r *= 10
            q, r = r // denominator, r % denominator
            if (q,r) in qr_map:
                rep_digit = qr_map[(q,r)]
                break
            qr_map[(q,r)] = len(digits)
            digits.append(q)
        def construct_decimals(digits, rep_digit):
            if rep_digit == -1: 
                return "".join([str(d) for d in digits])
            else:
                str1 = "".join([str(d) for d in digits[0:rep_digit]])                                                                                                             
                str2 = "".join([str(d) for d in digits[rep_digit:]])
                return str1 + "(" + str2 + ")" 
        decimal_str = "" if len(digits) == 0 else "." + construct_decimals(digits, rep_digit)
        sign_str = "" if positive else "-"
        return sign_str + str(int_q) + decimal_str

print Solution().fractionToDecimal(2, 3)
print Solution().fractionToDecimal(3, 1)
print Solution().fractionToDecimal(1, 7)

