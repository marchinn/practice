# [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching)

####
```python
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match=re.fullmatch(p,s) 
        return (True if match else False)
```