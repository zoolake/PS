import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # 그래프 생성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫번째 리프노드
        leaf_nodes = []
        for node in graph.keys():
            if len(graph[node]) == 1:
                leaf_nodes.append(node)
        
        # 반복적으로 리프노드 제거
        while n > 2:
            n -= len(leaf_nodes)
            new_leaf_nodes = []
            for leaf in leaf_nodes:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaf_nodes.append(neighbor)

            leaf_nodes = new_leaf_nodes
        
        return leaf_nodes
