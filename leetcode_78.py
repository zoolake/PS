class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def dfs(index, elem):
            if index == len(nums):
                return
                
            results.append(elem)
            for i in range(index, len(nums)):
                dfs(i+1, elem+[nums[i]])
            
        dfs(0,[])
        return results