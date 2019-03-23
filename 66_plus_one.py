class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # reverse
        # add one, propagate
        # reverse back
        digits = digits[::-1]
        carry = 1
        for i,v in enumerate(digits):
            tot = carry + v
            carry, digits[i] = tot // 10, tot % 10
            if carry == 0: break
        if carry != 0:
            digits.append(carry)
        return digits[::-1]
