import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            temp.append([dist, point])

        sorted_temp = sorted(temp, key= lambda x: x[0])
        result = []
        for i in range(k):
            result.append(sorted_temp[i][1])

        return result