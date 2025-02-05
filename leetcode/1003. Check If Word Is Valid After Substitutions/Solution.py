import re

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3 or not re.findall("abc", s):
            return False

        remainder = s.replace("abc", "")

        while "abc" in remainder:
            remainder = remainder.replace("abc", "")
            
        return remainder == ""