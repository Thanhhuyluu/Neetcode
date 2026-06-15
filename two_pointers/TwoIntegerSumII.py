# https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1
        while head < tail:
            sum = numbers[head] + numbers[tail]
            if sum == target:
                return [head+1, tail+1]
            if sum > target:
                tail-=1
            if sum < target:
                head += 1
        return []

numbers = [1,2,3,4]
target = 3
solution = Solution()
print(solution.twoSum(numbers,target))


