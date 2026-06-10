# https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        flag = 0
        result = []
        for i in nums:                
            if i == 0:
                flag += 1
            else:
                temp = temp * i
        for i in nums:
            if flag ==1:
                if i == 0:
                    result.append(temp)
                else:
                    result.append(0)
            elif flag > 1:
                result.append(0)
            else:
                result.append(int(temp / i))
        

        return result

s = Solution()

print(s.productExceptSelf([1,2,4,6]))
print(s.productExceptSelf([-1,0,1,2,3]))

print(s.productExceptSelf([0,8,0]))
