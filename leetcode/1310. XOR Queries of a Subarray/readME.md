# (1310. XOR Queries of a Subarray)[https://leetcode.com/problems/xor-queries-of-a-subarray]

####
```python
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for num in arr:
            prefix.append(num ^ prefix[-1])

        answer = []
        for left, right in queries:
            res = prefix[right + 1] ^ prefix[left]
            answer.append(res)

        return answer
```