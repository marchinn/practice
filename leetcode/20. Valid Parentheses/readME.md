# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

####
```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}

        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            elif not stack or brackets[bracket] != stack.pop():
                return False
        
        return len(stack) == 0
```