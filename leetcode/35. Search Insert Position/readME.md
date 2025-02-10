# [35. Search Insert Position](https://leetcode.com/problems/search-insert-position)

####
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if nums[0] > target:
                return 0

            n = None
            for i in range(len(nums)):
                if nums [i] > target:
                    n = i
                    break
```