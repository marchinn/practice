# [2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays)

####

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        diff=[list(set(nums1)-set(nums2)),list(set(nums2)-set(nums1))]
        return (diff)
```