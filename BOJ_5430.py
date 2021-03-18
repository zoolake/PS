T = int(input())

for i in range(T):
    command = input()   # 명령
    n = int(input())    # 요소 개수
    error = False
    rev_state = False
    front_cnt = 0
    rear_cnt = 0

    if n == 0:
        input()
        arr = []
    elif n > 0:
        arr = list(map(int, input()[1:-1].split(',')))   # 배열

    for ch in command:
        if ch == 'R':
            if n == 0:
                continue
            else:
                rev_state = not rev_state

        elif ch == 'D':
            if n == 0:
                print('error')
                error = True
                break
            else:
                if rev_state:
                    rear_cnt += 1
                else:
                    front_cnt += 1
                n -= 1

    if not error:
        if rev_state:
            print(str(arr[-rear_cnt-1:-rear_cnt-1-n:-1]).replace(' ', ''))
        else:
            print(str(arr[front_cnt:front_cnt+n]).replace(' ', ''))
