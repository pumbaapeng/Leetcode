class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 0
        prev_prev = 0
        prev = 1
        for i in range(0, len(s)):
            n_1gram = 1 if s[i] != '0' else 0
            n_2gram = 1 if i != 0 and (s[i-1] == '1' or s[i-1] == '2') and int(s[(i-1):(i + 1)]) >= 10 and int(s[(i-1):(i + 1)]) <= 26 else 0
            cur = n_1gram * prev + n_2gram * prev_prev
            prev_prev, prev = prev, cur
        return prev
