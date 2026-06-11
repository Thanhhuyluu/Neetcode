
# https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        result = sorted(freq.items(), key=lambda x : x[1], reverse=True )
        return [num for num, count in result[:k]]
s = Solution()
print(s.topKFrequent([1,2,2,3,3,3], k=2))
