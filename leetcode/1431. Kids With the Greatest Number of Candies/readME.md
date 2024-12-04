# [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies)

####
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        for c in candies:
            if c+extraCandies>=max(candies):
                result.append(True)
            else:
                result.append(False)
        return []
```