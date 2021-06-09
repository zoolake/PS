# 실수한 부분
#   1) floor-d 해야하는데, floor-u 로 작성함.
#   2) if / if 로 해야하는데, if / elif 로 함.
#       => 두 조건 모두 확인하고 큐에 삽입하던가 해야하는데,
#           if / elif 로 하면 많아도 두 조건 중 하나만 처리하는 상황이 생긴다.
#   3) 디버깅용 print 지우다가 결과 print도 지워버림. 
from collections import deque

f, s, g, u, d = map(int,input().split())
q = deque([(s,0)])
visited = [False] * (f+1)
visited[s] = True

while q:
    floor, time = q.popleft()
    # 도착
    if floor == g:
        print(time)
        break
    # U 버튼
    if 1<= floor + u<= f and not visited[floor+u]:
        visited[floor+u] = True
        q.append((floor+u, time+1))
    # D 버튼
    if 1<= floor - d<= f and not visited[floor-d]:
        visited[floor-d] = True
        q.append((floor-d, time+1))

else:
    print('use the stairs')