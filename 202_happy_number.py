class Solution(object):
    def isHappy(self, n):
        def get_next_num(n):
            sum = 0
            while n > 0:
                r, n = n % 10, n // 10
                sum += r*r
            return sum
        mem = set()
        n = get_next_num(n)
        while n not in mem:
            if n == 1:
                return True
            mem.add(n)
            n = get_next_num(n)
        return False


if __name__ == '__main__':
    print Solution().isHappy(1)
    print Solution().isHappy(19)
    print Solution().isHappy(3)
    print Solution().isHappy(2)
