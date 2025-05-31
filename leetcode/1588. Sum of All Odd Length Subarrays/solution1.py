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