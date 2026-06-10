# https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        done = []
        for i in nums:
            if i in done:
                return True
            else:
                done.append(i)
        return False
        
