class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = 0
        for num in nums:
            if num % 3 == 0:
                continue
            
            if (num - 1) % 3 == 0:
                n += 1
            elif (num + 1) % 3 == 0:
                n += 1
            
        return n