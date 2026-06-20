# https://neetcode.io/problems/eating-bananas/question?list=neetcode150
from typing import List
import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        l = 1 
        r = max_piles 
        result = max_piles

        
        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = min(result, k)
                r = k -1 
            else:
                l = k + 1
        return result

            



solution = Solution()
piles = [1,4,3,2]
h = 9
print(solution.minEatingSpeed(piles, h))
        
piles = [25,10,23,4]
h = 4
print(solution.minEatingSpeed(piles, h))

