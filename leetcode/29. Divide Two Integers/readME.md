# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers)

####
```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        regulator = 1
        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            regulator = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = (dividend // divisor) * regulator

        if quotient < -2**31:
            return -2**31
        if quotient > 2**31 - 1:
            return 2**31 - 1

        return quotient
```