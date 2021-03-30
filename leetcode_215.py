import heapq
# 1. 최대 힙
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []
#         for num in nums:
#             heapq.heappush(heap, (-num, num))
        
#         for _ in range(k-1):
#             heapq.heappop(heap)
        
#         return heapq.heappop(heap)[1]

# 2. nlargest 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]