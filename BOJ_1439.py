s = list(map(int, input()))
table = [0]*2
for index in range(len(s)):
    if index == 0 or s[index] != s[index-1]:
        table[s[index]] += 1

print(min(table[0],table[1]))
