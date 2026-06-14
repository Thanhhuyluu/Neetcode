# https://neetcode.io/problems/daily-temperatures/question?list=neetcode150
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 * n for n in range(len(temperatures))]
        for i in range(len(temperatures)-1):
            for j in range(i, len(temperatures)): 
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result        

# stack approach:

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 * n for n in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result        


                
solution = Solution()

temperatures = [30,38,30,36,35,40,28]
print(solution.dailyTemperatures(temperatures))
temperatures = [22,21,20]
print(solution.dailyTemperatures(temperatures))
