# [2485. Find the Pivot Integer](https://leetcode.com/problems/find-the-pivot-integer)

####
```python
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        prefix = [1]
        for i in range(2, n + 1):
            prefix.append(prefix[-1] + i)
        
        totalSum = prefix[-1]
        for x in range(1, n + 1):
            leftSum = prefix[x - 1]
            rightSum = totalSum - prefix[x - 1] + x
            if leftSum == rightSum:
                return x
        
        return -1
```