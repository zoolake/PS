class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            dic[num] = idx
        
        for idx, num in enumerate(nums):
            if target-num in dic and idx != dic[target-num]:
                return nums.index(num), dic[target-num]
        
