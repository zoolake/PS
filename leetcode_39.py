class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def dfs(temp, index):
            if sum(temp) > target:               
                return
            if sum(temp) == target:
                results.append(temp[:])
                print(temp)
                return

            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                dfs(temp, i)
                temp.pop()
    
        dfs([], 0)
        return results