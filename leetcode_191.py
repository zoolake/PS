# 1. 1의 개수 카운트
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count('1')

# 2. 비트 연산
class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            n &= n - 1
            cnt += 1
        return cnt