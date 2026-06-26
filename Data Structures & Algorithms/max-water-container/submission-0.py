class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        n = len(heights)
        right = n - 1
        max_water = 0
        while left < right:
            width = right - left
            area = width*min(heights[left],heights[right])
            max_water = max(area,max_water)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water


            


        