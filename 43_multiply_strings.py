class Solution:
    @staticmethod
    def remove_trailing_zeros(s):
        for i in range(len(s) - 1, -1, -1):
            if i != 0 and s[i] == '0':
                s = s[:-1]
            else:
                return s
        return s
    
    @staticmethod
    def one_digit_mul(d, num):
        carry = 0
        ret = ""
        for i in range(len(num)):
            c = num[i]
            tmp = int(c) * int(d) + carry
            carry, cur = tmp // 10, tmp % 10
            ret += str(cur)
        if carry != 0:
            ret += str(carry)
        ret = Solution.remove_trailing_zeros(ret)
        return ret
            
    @staticmethod
    def add_two(num1, num2):
        ret = ""
        carry = 0
        for i in range(max(len(num1), len(num2))):
            n1 = int(num1[i]) if i < len(num1) else 0
            n2 = int(num2[i]) if i < len(num2) else 0
            tmp = n1 + n2 + carry
            carry, r = tmp // 10, tmp % 10
            ret += str(r)
        if carry > 0:
            ret += str(carry)
        ret = Solution.remove_trailing_zeros(ret)
        return ret
        
    def multiply(self, num1: str, num2: str) -> str:
        assert(len(num1) >= 1 and len(num2) >= 1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        ret = "0"
        for i in range(len(num2)):
            c = num2[i]
            tmp = ('0' * i) + Solution.one_digit_mul(c, num1)
            ret = Solution.add_two(ret, tmp)
        return ret[::-1]
