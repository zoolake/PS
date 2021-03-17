class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        queue = [(0,k)] # (시간, 노드)
        dist = collections.defaultdict(int)

        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    temp = time + w
                    heapq.heappush(queue, (temp, v))
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1
        