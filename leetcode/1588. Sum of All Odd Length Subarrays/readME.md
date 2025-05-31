# [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays)

#### Solution 1
```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # with prefix sum

        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        res = 0
        n = len(prefix)
        for i in range (n):
            for j in range (i + 1, n, 2):
                res += prefix[j] - prefix[i]
    
        return res
```

#### Solution 2
```python
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range (len(arr)):
            subArray = []
            for j in range (i, len(arr)):
                subArray.append(arr[j])
                if len(subArray) % 2 != 0:
                    res += sum(subArray)
        return res
```