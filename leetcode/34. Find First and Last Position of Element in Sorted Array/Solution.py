class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        start = nums.index(target)
        end = start
        while target in nums:
            nums.remove(target)
            end += 1

        return [start, end-1]