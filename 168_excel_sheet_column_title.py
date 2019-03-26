class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = ""
        while n > 0:
            r = n % 26
            if r == 0:
                ret += 'Z'
                n -= 1
            else:
                ret += chr(ord('A') + r - 1)
            n //= 26
        return ret[::-1]

if __name__ == '__main__':
    print(Solution().convertToTitle(701))
