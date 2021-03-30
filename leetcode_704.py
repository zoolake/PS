import bisect
# 1. 반복을 통한 이진탐색
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > target:
#                 right = mid
#             elif nums[mid] < target:
#                 left = mid
#             elif nums[mid] == target:
#                 return mid      
#         return -1

# 2. 이진 검색 모듈
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        if 0<= idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1