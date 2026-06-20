class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        area=0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                ind, height = stack.pop()
                area = max(area, height*(i - ind))
                start = ind
            stack.append((start, h))

        for i, h in stack:
            area  = max(area, h*(len(heights) - i))
        return area