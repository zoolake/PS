import sys
import collections


def ripen() -> int:
    already_ripen = True
    days = 0
    queue = collections.deque()

    for h in range(H):
        for y in range(Y):
            for x in range(X):
                if boxes[h][y][x] == 1:
                    queue.append([h, y, x])
                elif boxes[h][y][x] == 0:
                    already_ripen = False

    if already_ripen:
        return 0
    else:
        days = bfs(queue)
        for h in range(H):
            for y in range(Y):
                for x in range(X):
                    if boxes[h][y][x] == 0:
                        return -1
        return days


def bfs(queue):
    days = -1   # 마지막에 큐에 담겨있는 좌표도 수행되기 때문에 불필요하게 하루가 더 추가되므로
    temp = collections.deque()

    while queue:
        for box in queue:
            x, y, h = box[2], box[1], box[0]
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nh = h + dh[i]
                if -1 < nx < X and -1 < ny < Y and -1 < nh < H and boxes[nh][ny][nx] == 0:
                    boxes[nh][ny][nx] = 1
                    temp.append([nh, ny, nx])

        days += 1
        queue = temp
        temp = collections.deque()

    return days


dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

input = sys.stdin.readline
X, Y, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(Y)] for _ in range(H)]

print(ripen())
