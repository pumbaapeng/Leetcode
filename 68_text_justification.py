class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        cur_words = []
        cur_chars = 0
        i = 0
        for word in words:
            if not Solution.fit(cur_words, cur_chars, word, maxWidth):
                ret.append(Solution.dump_reg(cur_words, cur_chars, maxWidth))
                cur_chars = 0
                cur_words = []
            cur_words.append(word)
            cur_chars += len(word)
        if len(cur_words) > 0:
            ret.append(Solution.dump_last(cur_words, cur_chars, maxWidth))
        return ret
            
    @staticmethod
    def dump_reg(cur_words, cur_chars, maxWidth) -> string:
        if len(cur_words) == 1:
            return cur_words[0] + " " * (maxWidth - len(cur_words[0]))
        n_breaks = len(cur_words) - 1
        tot_spaces = maxWidth - cur_chars
        spaces_per_break = tot_spaces // n_breaks
        excess = tot_spaces % n_breaks
        line = ""
        for i, word in enumerate(cur_words):
            if i == 0:
                line += word
            else:
                n_spaces = spaces_per_break + (1 if excess > 0 else 0)
                excess -= 1
                spaces = " " * n_spaces
                line += (spaces + word)
        return line
    
    @staticmethod
    def dump_last(cur_words, cur_chars, maxWidth) -> string:
        line = " ".join(cur_words)
        trailing_spaces = " " * (maxWidth - len(line))
        line += trailing_spaces
        return line
        
    @staticmethod
    def fit(cur_words, cur_chars, word, maxWidth) -> string:
        if cur_chars + len(cur_words) + len(word) <= maxWidth:
            return True
        return False
