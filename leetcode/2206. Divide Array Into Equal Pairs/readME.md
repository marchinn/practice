# [2206. Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs)

####
```python
import collections
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt=Counter(nums)
        if len(nums)%2==0 and all(cnt.get(num)%2==0 for num in cnt):
            return True
        else:
            return False
```