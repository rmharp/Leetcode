### Roman to Integer - Completed July 21st, 2024
## Runtime of 41 ms beats 83.38%
## Memory of 16.63 MB beats 9.56%

class Solution:
    def romanToInt(self, s: str) -> int:
        romantointdict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
        }
        ssstr = str(s)
        slen = len(ssstr)
        i = 0
        finalint = 0
        while i < slen:
            checkedstr = s[i]
            if (i + 1 < slen) and (checkedstr == "C" and (s[i + 1] == "D" or s[i + 1] == "M")):
                checkedstr = f"{s[i]}{s[i + 1]}"
                i += 1
            elif (i + 1 < slen) and (checkedstr == "X" and (s[i + 1] == "L" or s[i + 1] == "C")):
                checkedstr = f"{s[i]}{s[i + 1]}"
                i += 1
            elif (i + 1 < slen) and (checkedstr == "I" and (s[i + 1] == "V" or s[i + 1] == "X")):
                checkedstr = f"{s[i]}{s[i + 1]}"
                i += 1
            finalint += romantointdict[checkedstr]
            i += 1
        return finalint
        
