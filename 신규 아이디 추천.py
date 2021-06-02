def check(x):
    if 'a'<=x<='z' or '0'<=x<='9' or x=='-' or x=='_' or x=='.':
        return True

def solution(new_id):
    answer = ''
    # 1단계
    answer = new_id.lower()
    # 2단계
    answer = list(filter(check, answer))
    # 3단계
    i = 0
    while True:
        if i >= len(answer)-1:
            break
        if answer[i] == '.' and answer[i+1] == '.':
            answer.pop(i)
            continue
        i+=1 
    # 4단계
    if answer and answer[0] == '.':
        answer.pop(0)
    if answer and answer[-1] == '.':
        answer.pop(-1)
    # 5단계
    if not answer:
        answer = ['a']
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer.pop()
    # 7단계
    last = answer[-1]
    if len(answer) <= 2:
        while len(answer) < 3:
            answer.append(last)

    answer = ''.join(answer)
    return answer