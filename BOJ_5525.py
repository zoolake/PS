# 문자열리스트 슬라이싱으로 접근 -> 시간초과
# 참고) https://codedrive.tistory.com/361
import sys

input = sys.stdin.readline
N = int(input())    # N=1 , IOI / N=2 , IOIOI
M = int(input())
S = input()

i = 1
pattern = 0
result = 0

while i < M-1:
    # 패턴이 존재하는 경우
    if S[i-1] + S[i] + S[i+1] == 'IOI':
        pattern += 1
        # 패턴의 갯수가 N과 동일한 경우
        if pattern == N:
            pattern -= 1
            result += 1
        i += 2
    
    else:
        pattern = 0
        i += 1
        
print(result)
