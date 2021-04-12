import collections
# 1. 슬라이딩 윈도우 + 브루트 포스
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         result = []
#         for index in range(len(nums)-(k-1)):
#             result.append(max(nums[index:index+k]))
#         return result

# 2. 슬라이딩 윈도우 + 큐를 이용한 최적화
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()
        max_value = float('-inf')
        

        for index, value in enumerate(nums):
            window.append(value)
            if index < k-1:
                continue
            
            if max_value == float('-inf'):
                max_value = max(winodw)
            elif value > max_value:
                max_value = value

            result.append(max_value)
            front = window.popleft()

            if front == max_value:
                max_value = float('-inf')
        
        return result
            


            