import sys

diff_y = [-1, 1, 0, 0]
diff_x = [0, 0, -1, 1]

# dfs
def DFS(y, x, length, total):
    global result

    if length >= 4:
        result = max(result, total)
        return

    for dy, dx in zip(diff_y, diff_x):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            DFS(ny, nx, length+1, total+paper[ny][nx])
            visited[ny][nx] = False

# dfs로 탐색할 수 없는 부분 처리(ㅏ,ㅓ,ㅗ,ㅜ)
def exception_handle(y, x, value):
    global result
    # ㅏ
    if 0<= y+2 < N and 0<= x+1 < M:
        total = value + paper[y+1][x] + paper[y+1][x+1] + paper[y+2][x]
        result = max(result, total)
    # ㅓ
    if 0 <= y-1 < N and 0<= y+1 < N and 0 <= x+1 < M:
        total = value + paper[y-1][x+1] + paper[y][x+1] + paper[y+1][x+1]
        result = max(result, total)
    # ㅗ
    if 0 <= y-1 < N and 0<= x+2 < M:
        total = value + paper[y-1][x+1] + paper[y][x+1] + paper[y][x+2]
        result = max(result, total)
    # ㅜ
    if 0<= y+1 < N and 0<= x+2 < M:
        total = value + paper[y+1][x+1] + paper[y][x+1] + paper[y][x+2]
        result = max(result, total)


input = sys.stdin.readline
N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, paper[i][j])
        visited[i][j] = False

        exception_handle(i, j, paper[i][j])

print(result)
