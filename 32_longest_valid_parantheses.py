class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ret = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append((i, c))
            else:
                if len(stack) > 0 and stack[-1][1] == '(':
                    stack.pop()
                    l_bound = -1 if len(stack) == 0 else stack[-1][0]
                    ret = max(i - l_bound, ret)
                else:
                    stack.append((i,c))
        return ret
