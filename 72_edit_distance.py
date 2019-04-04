class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev_line = list(range(len(word1) + 1))
        for i in range(1, len(word2) + 1):
            cur_line = [i for col in range(len(word1) + 1)]
            for j in range(1, len(word1) + 1):
                left_up = prev_line[j - 1] + (0 if word1[j - 1] == word2[i - 1] else 1)
                left = cur_line[j - 1] + 1
                up = prev_line[j] + 1
                cur_line[j] = min(left, up, left_up)
            prev_line = cur_line
        return prev_line[-1]
