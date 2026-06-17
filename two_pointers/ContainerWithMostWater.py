# https://neetcode.io/problems/max-water-container/question?list=neetcode150
from typing import List, runtime_checkable
class Solution:

    # def maxArea(self, heights: List[int]) -> int:
    #     max  = 0
    #     for i in range(len(heights)-1):
    #         for j in range(i +1, len(heights)):
    #             temp = min(heights[i],heights[j]) * (j-i)
    #             if temp > max:
    #                 max = temp 
    #     return max
    #
    #
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            temp = min(heights[l], heights[r]) * (r - l)
            if temp > max:
                max = temp

            if heights[l] < heights[r]:
                l +=1

            else:
                r-=1
        return max
solution = Solution()
height = [1,7,2,5,4,7,3,6]
print(solution.maxArea (height))
