import heapq

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    heapq.heappush(heap, (-num, num))

while heap:
    print(heapq.heappop(heap)[1], end=' ')