pos = input()
row = int(pos[1])
col = ord(pos[0]) - ord('a') + 1
move_list = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
result = 0
for move in move_list:
    nrow = row + move[0]
    ncol = col + move[1]
    if 1 <= nrow <= 8 and 1 <= ncol <= 8:
        result += 1 
print(result)