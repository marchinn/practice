# [1. Two Sum](https://leetcode.com/problems/two-sum)
####
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    sums.append(i)
                    sums.append(j)
                    return sums
```