import re

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s or s.strip() == '':
            return 0

        i = 0
        s = s.strip()
        if s[0] == '-':
            sign = -1
            i += 1
        else:
            sign = 1
            if s[0] == '+':
                i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        if result < (-2)**31:
            return (-2)**31
        elif result > (2**31)-1:
            return (2**31)-1
        
        return result