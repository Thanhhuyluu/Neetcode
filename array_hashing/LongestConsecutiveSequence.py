# https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        temp = {}
        j = 0
        
        sorted_nums = list(set(sorted_nums))
        if len(sorted_nums) == 0 or len(sorted_nums) == 1:

            return len(sorted_nums)

        print(sorted_nums)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                temp[j] = i+1
            else:
                j+=1
        max = 0        
        index = 0
        for i in range(len(temp)):

            if (temp[i] - i) > max:
                max = temp[i] - i
                index = i

        return len(sorted_nums[index: temp[index] + 1])


s = Solution()

nums = [2,20,4,10,3,4,5]
print(s.longestConsecutive(nums))
nums = [0,3,2,5,4,6,1,1]
print(s.longestConsecutive(nums))


