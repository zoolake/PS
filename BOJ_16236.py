import sys
import collections

input = sys.stdin.readline
diff_x = [-1,1,0,0]
diff_y = [0,0,-1,1]

# BFS
def BFS(x, y):
    q = collections.deque()
    visited = set()
    weight = 2
    time = 0
    count = 0
    flag = False
    result = 0

    q.append((x,y))
    visited.add((x,y))

    while q:
        q = collections.deque(sorted(q))
        
        for _ in range(len(q)):
            x, y = q.popleft()

            # 상어를 먹는 경우
            if 0 < area[x][y] < weight:
                count += 1
                area[x][y] = 0
                # 먹은 횟수가 무게와 같은 경우
                if count == weight:
                    weight += 1
                    count = 0
                
                # 먹은지점 기준으로 다시 주변 탐색
                q, visited = collections.deque(), set([(x,y)])
                flag = True
                result = time

            for dx,dy in zip(diff_x, diff_y):
                nx, ny = x+dx, y+dy
                if 0<= nx < N and 0<= ny < N and (nx,ny) not in visited:
                    if area[nx][ny] <= weight:
                        q.append((nx,ny))
                        visited.add((nx,ny))

            if flag:
                flag = False
                break
        
        time += 1
    print(result)

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            x, y = i, j
            area[i][j] = 0
            break

BFS(x, y)