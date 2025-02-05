# [1003. Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions)

####
```python
import re

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3 or not re.findall("abc", s):
            return False

        remainder = s.replace("abc", "")

        while "abc" in remainder:
            remainder = remainder.replace("abc", "")
            
        return remainder == ""
```