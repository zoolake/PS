# 1)틀린 부분
#   if board[nx][ny] != 0:  
# 2)수정
#   elif board[nx][ny] != 0:
# 3)잘못한 점
#   무분별하게 if + if 로 작성하다가 연속적으로 조건문을 거치는 상황이 생김


import sys
input = sys.stdin.readline

def rotation(d, direction) :
    if direction == 1:
        rotated_object = [d[0],d[4],d[2],d[5],d[3],d[1]]        
    if direction == 2:
        rotated_object = [d[0],d[5],d[2],d[4],d[1],d[3]]
    if direction == 3:
        rotated_object = [d[1],d[2],d[3],d[0],d[4],d[5]]
    if direction == 4:
        rotated_object = [d[3],d[0],d[1],d[2],d[4],d[5]]

    return rotated_object
    
n, m, x, y, k = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
operations = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]   # 인덱스1 = 윗면 / 인덱스3 = 아랫면
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
for op in operations:
    nx, ny = x + dx[op], y+ dy[op]
    if 0<= nx < n and 0<= ny < m:
        dice = rotation(dice, op)
        # 칸의 숫자가 0이라면
        if board[nx][ny] == 0:
            # 주사위 바닥면의 숫자를 칸에 복사
            board[nx][ny] = dice[3]
            
        # 칸의 숫자가 0이 아니라면
        elif board[nx][ny] != 0:
            # 칸의 숫자를 주사위 바닥면으로 복사 후, 칸의 숫자는 0
            dice[3] = board[nx][ny]
            board[nx][ny] = 0

        # 주사위 위치 변경
        x, y = nx, ny
        print(dice[1])