import sys
import copy
from collections import deque

n = int(input())
# 진입차수, 그래프, 강의 시간 초기화
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
# 입력
for i in range(1, n+1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for j in range(1, len(info)-1):
        graph[info[j]].append(i)
        indegree[i] += 1  
# 위상정렬
def topology():
    result = copy.deepcopy(time)
    q = deque()
    # 진입차수가 0이면 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            indegree[i] -= 1
            result[i] = max(result[i], time[i] + result[node])
            if indegree[i] == 0:
                q.append(i)
    
    # 출력
    for i in range(1, n+1):
        print(result[i])

topology()
