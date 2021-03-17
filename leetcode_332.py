class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for From, To in sorted(tickets):
            graph[From].append(To)
        
        results = []
        def dfs(From):
            while graph[From]:
                next = graph[From].pop(0)
                dfs(next)
            results.append(From)
        
        dfs("JFK")
        return reversed(results)

