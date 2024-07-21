### Valid Parentheses - Completed July 21st, 2024
## Runtime of 39 ms beats 31.46%
## Memory of 16.60 MB beats 11.01%

class Solution:
    def isValid(self, s: str) -> bool:
        strlen = len(s)
        if not s or strlen % 2 != 0:
            return False
        stack = []
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                return False
        return len(stack) == 0
