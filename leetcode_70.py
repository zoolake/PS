# # 1. 타뷸레이션(상향식)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [0,1,2,3]
#         for i in range(4,n+1):
#             dp.append(dp[i-1] + dp[i-2])
        
#         return dp[n]

# 2. 메모이제이션(하향식)
import collections
class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        

