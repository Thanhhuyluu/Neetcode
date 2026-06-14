# https://neetcode.io/problems/car-fleet/question?list=neetcode150
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) 
        stack = []
        for p, s in cars:
            if not stack or ((target - p) / s) > stack[-1]:
                stack.append((target - p) / s)
        return len(stack)

solution = Solution()
target = 10
position = [1,4]
speed = [3,2]
print(solution.carFleet(target, position, speed))
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
print(solution.carFleet(target, position, speed))


