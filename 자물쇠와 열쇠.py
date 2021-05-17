import copy
def rotation(key):
    copy_key = copy.deepcopy(key)
    M = len(key)
    for i in range(M):
        for j in range(M):
            copy_key[i][j] = key[M-j-1][i]
    return copy_key
    
def check(key, lock, key_row, key_col, start, end, extended):
    N = len(lock)
    M = len(key)
    extended_board = [[0]*extended for _ in range(extended)]
    # extended_board 중심에 lock 삽입
    for i in range(N):
        for j in range(N):
            extended_board[start+i][start+j] += lock[i][j]

    # 이동
    for row in range(M):
        for col in range(M):
            extended_board[key_row+row][key_col+col] += key[row][col]
    
    # 검사
    for i in range(start,end):
        for j in range(start,end):
            if extended_board[i][j] == 0 or extended_board[i][j] == 2:
                return False
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    extended = N + 2*(M-1)
    lock_start = M - 1
    lock_end = lock_start + N
    for _ in range(4):
        key = rotation(key)
        for i in range(lock_end):
            for j in range(lock_end):
                if check(key, lock, i, j, lock_start, lock_end, extended):
                    return True
    return False