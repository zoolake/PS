from collections import deque

a, b = map(int, input().split())
q = deque([(a,0)])
result = -1
while q:
    num, count = q.popleft()
    if num == b:
        result = count + 1 
        break

    new_num1, new_num2 = num * 2, int(str(num)+'1')
    if new_num1 <= b:
        q.append((new_num1, count+1))
    if new_num2 <= b:
        q.append((new_num2, count+1))

print(result)
