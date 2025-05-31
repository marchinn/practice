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