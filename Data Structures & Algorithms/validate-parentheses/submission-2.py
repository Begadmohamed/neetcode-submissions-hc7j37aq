class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "}":
                if not stack or stack[-1]!="{":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if not stack or stack[-1]!="[":
                    return False
                else:
                    stack.pop()
            elif char == ")":
                if not stack or stack[-1]!="(":
                    return False
                else:
                    stack.pop()
            elif char in "([{":
                stack.append(char)
        if  not stack:
            return True
        else:
            return False

