class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low = 0
        high = len(heights) - 1
        maxArea = 0
        while low < high:
            
            w = high - low
            if heights[low] < heights[high]:
                h = heights[low]
                low+=1
            else:
                h = heights[high]
                high-=1
            maxArea = max(h*w , maxArea)
        return maxArea

        