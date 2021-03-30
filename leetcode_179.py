class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        idx = 0
        while idx < len(nums):
            pointer = idx
            while pointer > 0 and \
                str(nums[pointer])+str(nums[pointer-1]) > str(nums[pointer-1]) + str(nums[pointer]):
                nums[pointer], nums[pointer-1] = nums[pointer-1], nums[pointer]
                pointer -= 1
            
            idx += 1
        
        return str(int(''.join(map(str,nums))))