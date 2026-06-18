# https://neetcode.io/problems/binary-search/question?list=neetcode150
from re import search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1 
        
        while l <= r:
            m =(l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            else:
                l = m+1
        return -1
            

solution = Solution()
nums = [-1,0,2,4,6,8]
target = 4

print(solution.search(nums, target))

nums = [-1,0,2,4,6,8]
target = 3
print(solution.search(nums, target))


