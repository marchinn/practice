class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        res = min(prefix)
        return abs(res) + 1