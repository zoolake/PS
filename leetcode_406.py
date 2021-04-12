import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        max_heap = []
        result = []
        for person in people:
            heapq.heappush(max_heap, (-person[0], person[1]))
        
        while max_heap:
            person = heapq.heappop(max_heap)
            result.insert(person[1], [-person[0], person[1]])
        
        return result
