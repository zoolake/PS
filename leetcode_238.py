class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 나눗셈 사용하지않고 O(n)
        # 각 인덱스의 왼쪽 오른쪽에 위치한 수들의 곱
        result = []
        left = []
        right = []

        for idx in range(len(nums)):
            if idx == 0:
                left.append(1)
            else:
                left.append(left[idx-1] * nums[idx-1])
        
        for idx in reversed(range(len(nums))):
            if idx == len(nums) - 1:
                right.append(1)
            else:
                right.insert(0,right[0]*nums[idx+1])

        for idx in range(len(nums)):
            result.append(left[idx] * right[idx])
        
        return result
            

