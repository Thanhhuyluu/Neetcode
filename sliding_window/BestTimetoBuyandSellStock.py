# https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150
from typing import List
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     max = 0 
    #     for i in range(len(prices)-1):
    #         for j in range(i, len(prices)):
    #             if prices[j] - prices[i] > max:
    #                  max = prices[j] - prices[i]
    #     return max
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        smallest = prices[0]
        for i in range(len(prices)):

            smallest = min(smallest, prices[i])
            maxProfit = max(maxProfit, prices[i] - smallest) 
        return maxProfit


solution = Solution()
print(solution.maxProfit( prices = [10,1,5,6,7,1]))
