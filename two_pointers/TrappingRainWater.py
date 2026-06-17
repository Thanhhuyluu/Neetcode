# https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1

        return water       
solution = Solution()
height = [0,2,0,3,1,0,1,3,2,1]
print(solution.trap(height))
        
