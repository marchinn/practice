# [2389. Longest subsequence With Limited Sum](https://leetcode.com/problems/longest-subsequence-with-limited-sum)

####
```python
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = []
        nums.sort()
        numSum = 0
        for num in nums:
            numSum += num
            prefix.append(numSum)

        answer = []
        for query in queries:
            filteredPrefix = [x for x in prefix if x <= query]
            answer.append(len(filteredPrefix))

        return answer
```