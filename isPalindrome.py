### Palindrome Number - Completed July 21st, 2024
## Runtime of 56 ms beats 47.63%
## Memory of 16.53 MB beats 32.91%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        xstr = str(x)
        stacklen = len(xstr)
        stack = []
        for i in range(stacklen // 2):
            stack.append(xstr[i])
        start_index = (stacklen // 2) if stacklen % 2 == 0 else (stacklen // 2 + 1)
        for i in range(start_index, stacklen):
            if xstr[i] != stack.pop():
                return False
                
        return True
