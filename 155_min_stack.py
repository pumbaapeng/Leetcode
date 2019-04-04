class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n_stack = []
        self.min_idx_stack = []
        
    def push(self, x: int) -> None:
        self.n_stack.append(x)
        if x < self.getMin():
            self.min_idx_stack.append(len(self.n_stack) - 1)

    def pop(self) -> None:
        self.n_stack.pop()
        min_idx = self.min_idx_stack[-1]
        if min_idx == len(self.n_stack):
            self.min_idx_stack.pop()
        
    def top(self) -> int:
        return self.n_stack[-1]

    def getMin(self) -> int:
        if len(self.min_idx_stack) == 0:
            return float('inf')
        return self.n_stack[self.min_idx_stack[-1]]
