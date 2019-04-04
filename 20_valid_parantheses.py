class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'[': ']', '{': '}', '(': ')'}
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if len(stack) > 0 and c == mapping[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
