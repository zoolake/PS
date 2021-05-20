# 실수한 부분
# 실수한 초기 코드: 
#   teachers = empty = []
#   if 조건
#       teachers.append(값)
#   if 조건
#       empty.append(값)
# 발생한 문제: 
# 처음에 "teachers = empty = []" 이 부분으로 인해 두 리스트가 같은 주소를 갖게 되는 상황
# 이 상황에서 조건문 별로 append 연산을 수행하더라도, 같은 주소를 갖기 때문에 최종적으로
# 완전히 같은 값을 갖게 된다. (애초에 같은 주소를 가진 상태인데, 거기다가 append 연산을 수행했기 때문)
# 해결 방법:
# 애초에 다른 객체이므로, 나눠서 선언해준다.
# teachers = [] / empty = []

# 저 부분에서 같은 주소를 갖는 상황이 생긴다는 것을 너무 늦게 인지했고 처음부터 의심을 갖지도 않음.
# 다음부터는 저런식으로 작성하는 것보다는 애초에 다른 객체로 사용될 상황이 일반적이므로 2줄에 나눠서
# 작성하는게 맞을듯하다.


# 풀이 1: DFS _ 192ms
import sys, copy
from itertools import combinations

input = sys.stdin.readline
n = int(input())
board = [list(input().split()) for _ in range(n)]

def dfs(board, row, col, dir):
    # 범위 내
    if 0<=row<n and 0<=col<n:
        if board[row][col] == 'O':
            return False
        elif board[row][col] == 'S':
            return True
        else:
            if dir == 0:    return dfs(board, row-1, col, dir)
            elif dir == 1:  return dfs(board, row+1, col, dir)
            elif dir == 2:  return dfs(board, row, col-1, dir)
            elif dir == 3:  return dfs(board, row, col+1, dir)
    # 범위 외
    else:
        return False

# 선생님 위치, 학생 위치, 빈 공간 위치 초기화
teachers = []
empty = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':  
            teachers.append((i,j))
        if board[i][j] == 'X':
            empty.append((i,j))

# 조합 생성
cmb = list(combinations(empty,3))
# 장애물 설치 후 dfs
impossible = True
for obstacles in cmb:
    copy_board = copy.deepcopy(board)
    
    # 장애물 설치
    for obstacle in obstacles:
        row, col = obstacle
        copy_board[row][col] = 'O'

    # DFS
    find_student = False
    for teacher in teachers:
        row, col = teacher
        for dir in range(4):
            find_student = dfs(copy_board, row, col, dir)
            if find_student:
                break
        if find_student:
            break

    if not find_student:
        impossible = False
        print('YES')
        break

if impossible:
    print('NO')
    

# # 풀이2: 단순 시뮬레이션 _ 196ms
# import sys, copy
# from itertools import combinations

# input = sys.stdin.readline
# n = int(input())
# board = [list(input().split()) for _ in range(n)]

# drow = [-1,1,0,0]
# dcol = [0,0,-1,1]

# # 선생님 위치, 학생 위치, 빈 공간 위치 초기화
# teachers = []
# empty = []
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 'T':  
#             teachers.append((i,j))
#         if board[i][j] == 'X':
#             empty.append((i,j))

# # 장애물 설치 후 검사
# impossible = True
# for obstacles in combinations(empty,3):
#     copy_board = copy.deepcopy(board)
    
#     # 장애물 설치
#     for obstacle in obstacles:
#         row, col = obstacle
#         copy_board[row][col] = 'O'
    
#     # 검사
#     find_student = False
#     for teacher in teachers:
#         for dir in range(4):
#             row, col = teacher
#             while 0<=row<n and 0<=col<n and copy_board[row][col]!='O':
#                 if copy_board[row][col] == 'S':
#                     find_student = True
#                     break
#                 row += drow[dir]
#                 col += dcol[dir]
#             if find_student:
#                 break
#         if find_student:
#             break

#     if not find_student:
#         impossible = False
#         print('YES')
#         break

# if impossible:
#     print('NO')
    



            








            




