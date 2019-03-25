class Solution:
    def myAtoi(self, s: str) -> int:
        sign, i = 1, 0
        my_min, my_max = (1 << 31) * -1, (1<<31) - 1
        while i < len(s) and s[i] == ' ':
            i += 1;
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = 1 if s[i] == '+' else -1
            i += 1
        my_sum = 0
        while i < len(s) and (s[i] >= '0' and s[i] <= '9'):
            my_sum = my_sum * 10 + int(s[i])
            i += 1
        my_sum = my_sum * sign
        if my_sum < my_min:
            return my_min
        elif my_sum > my_max:
            return my_max
        else:
            return my_sum