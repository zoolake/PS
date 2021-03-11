class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    # 1. 재귀를 이용한 풀이
        # result = []
        # temp = []

        # def dfs(elem: List[int]):
        #     # 탈출조건
        #     if len(elem) == 0:
        #         result.append(temp[:])
        #         return
            
        #     for e in elem:
        #         next = elem[:]
        #         next.remove(e)

        #         temp.append(e)
        #         dfs(next)
        #         temp.pop()
                       
        # dfs(nums)       
        # return result

    # 2. itertools 모듈을 이용한 풀이
        return list(itertools.permutations(nums))