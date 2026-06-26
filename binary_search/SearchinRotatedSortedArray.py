# https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150

from typing import List
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:

                return m
            if nums[l] <= nums[m]: # nua trai tang dan
                if nums[m] > target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]< target <= nums[r]:
                    l = m+1
                else:
                    r = m -1
        return -1
solution = Solution()

nums = [3,4,5,6,1,2]
target = 1
print(solution.search(nums,target))
nums = [3,5,6,0,1,2]
target = 4
print(solution.search(nums,target))


