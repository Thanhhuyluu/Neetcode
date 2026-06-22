# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m+1
            
            else:
                r = m-1
        return res

nums = [3,4,5,6,1,2]
solution = Solution()
print(solution.findMin(nums))
        
nums = [4,5,0,1,2,3]
print(solution.findMin(nums))
        
