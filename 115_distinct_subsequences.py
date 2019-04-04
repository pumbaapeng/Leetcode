class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev_row = [1 for i in range(len(s) + 1)]
        for i_t in range(len(t)):
            cur_row = [0 for j in range(len(s) + 1)]
            for col in range(1, len(s) + 1):
                i_s = col - 1
                n_use = prev_row[col - 1] if s[i_s] == t[i_t] else 0
                n_not_use = cur_row[col - 1]
                cur_row[col] = n_use + n_not_use
            prev_row = cur_row
        return prev_row[len(s)]
