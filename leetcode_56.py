class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_list = sorted(intervals, key= lambda x: x[0])
        result = []

        for i in new_list:
            if not result or result[-1][1] < i[0]:
                result += [i]
            elif result[-1][1] >= i[0]:
                result[-1][1] = max(result[-1][1],i[1])
        
        return result