def solution(s):
    if len(s) == 1:
        return 1
        
    max_type = len(s) // 2
    result = float('inf')

    for step in range(0, max_type):
        index = 0
        temp = ''
        prev_pattern = ''
        count = 0
        while index + step < len(s):
            pattern = s[index:index+step+1]
            if index == 0:
                prev_pattern = pattern
                count += 1
            else:
                if prev_pattern == pattern:
                    count += 1
                else:
                    temp += prev_pattern
                    if count >= 2:
                        temp += str(count)
                    prev_pattern = pattern
                    count = 1
            index += (step+1)

        temp += prev_pattern
        if count >= 2:
            temp += str(count)
        temp += s[index:]
        result = min(result, len(temp))
    return result
