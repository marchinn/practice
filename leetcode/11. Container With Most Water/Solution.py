class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        maxVolume = 0
        left = 0
        right = len(heights) - 1

        while left < right:               
                height = min(heights[left], heights[right])
                width = right - left
                volume = height * width

                if volume > maxVolume:
                    maxVolume = volume

                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1