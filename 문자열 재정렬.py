# 문자 입력
s = input()
# 순회
char = []
number = 0
for ch in s:
    if 'A'<= ch <= 'Z':
        char.append(ch)
    else:
        number += int(ch)
# 합치기
char.sort()
number = str(number)
print(''.join(char)+number)