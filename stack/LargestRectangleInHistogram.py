# https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i ))
        return maxArea
            


solution = Solution()
heights = [7,1,7,2,2,4]
print(solution.largestRectangleArea(heights))
