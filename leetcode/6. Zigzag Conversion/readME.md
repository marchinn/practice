# [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)

####
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or len(s) < numRows:
            return s

        rows = [''] * numRows
        index = 0
        step = 1

        for symbol in s:

            rows[index] += symbol

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        return ''.join(rows)
```