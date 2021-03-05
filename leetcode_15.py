class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        # 1개의 기준점과 2개의 포인터 사용
        for i in range(len(nums)-2):
            # 기준점이 동일한 경우 스킵
            if i>0 and nums[i]==nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    result.append((nums[i], nums[left], nums[right]))

                    # 동일한 숫자가 존재할 가능성이 있기 때문에 스킵
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    
                    right-=1
                    left+=1
        
        return result