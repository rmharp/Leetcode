### Longest Common Prefix - Completed July 21st, 2024
## Runtime of 38 ms beats 56.45%
## Memory of 16.63 MB beats 62.67%

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        commonpref = []
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != char:
                    return ''.join(commonpref)
            commonpref.append(char)
        
        return ''.join(commonpref)
