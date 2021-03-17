class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append([v,w])
        
        queue = [(0,src,K)]

        while queue:
            price, city, count = heapq.heappop(queue)
            if city == dst:
                return price
            if count >= 0:
                for v, w in graph[city]:
                    temp = price + w
                    heapq.heappush(queue, (temp, v, count-1))
        
        return -1