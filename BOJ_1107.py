import sys
N = int(input())    # 목표 채널
M = int(input())    # 고장난 버튼 수
wrong_buttons = list(map(int, sys.stdin.readline().split()))
buttons = set(num for num in range(10) if num not in wrong_buttons)

min_count = abs(N-100)

# 모든 버튼이 고장난 경우
if M == 10:
    print(min_count)

# 고장이 나지않은 경우
elif M == 0:
    print(min(min_count, len(str(N))))

# 브루트 포스
else:
    for channel in range(1000001):
        str_channel = str(channel)
        for idx in range(len(str_channel)):
            if int(str_channel[idx]) not in buttons:
                break
            elif idx == len(str_channel)-1:
                min_count = min(min_count, len(str_channel) + abs(N - channel))
    print(min_count)
