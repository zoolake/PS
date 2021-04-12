# 1. 일반
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         result = 0
#         for index in range(len(prices)-1):
#             profit = prices[index+1] - prices[index]
#             if  profit > 0:
#                 result += profit

#         return result
# 2. 파이썬다운 방식
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))
