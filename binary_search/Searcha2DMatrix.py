# https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                l = 0
                r = len(matrix[row]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if matrix[row][m] == target:
                        return True
                    elif matrix[row][m] < target:
                        l = m + 1
                    else:
                        r = m - 1

                return False

            elif target < matrix[row][0]:
                bot = row - 1
            else:
                top = row + 1

        return False                   
        

solution = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print(solution.searchMatrix(matrix, target))
        

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]] 
target = 15
print(solution.searchMatrix(matrix, target))


