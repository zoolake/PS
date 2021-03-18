import sys
M = int(input())
s = set()
for _ in range(M):
    line = sys.stdin.readline().split()
    command = line[0]

    # all, empty
    if len(line) == 1:
        if command == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
    else:
        x = int(line[1])
        if command == 'add' and x not in s:
            s.add(x)
        elif command == 'remove' and x in s:
            s.discard(x)
        elif command == 'check':
            print(int(x in s))
        elif command == 'toggle':
            if x in s:
                s.discard(x)               
            else:
                s.add(x)

# set에서 discard와 remove의 차이점
# discard는 없는 값을 지우려해도 에러가 발생하지 않는다.
# 반면, remove는 없는 값을 지우려하면 에러가 발생한다.