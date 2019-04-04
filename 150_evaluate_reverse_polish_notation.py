class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        stack = []
        for token in tokens:
            if self.is_digit(token):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append((abs(a) // abs(b)) * (1 if a * b >= 0 else -1))
        return stack[0]
    def is_digit(self, token):
        if token in {"+", "-", "*", "/"}:
            return False
        else:
            return True
