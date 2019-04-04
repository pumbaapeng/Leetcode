class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        my_stack = []
        for token in tokens:
            if token == "" or token == ".":
                continue
            elif token == "..":
                if len(my_stack) > 0:
                    my_stack.pop()
            else:
                my_stack.append(token)
        return "/" + "/".join(my_stack)
