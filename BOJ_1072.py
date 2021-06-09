x, y = map(int, input().split())
z = (y*100)/x

left, right = 1, 1000000000
while left <= right:
    mid = (left+right)//2
    new_z = int(((y+mid)*100/(x+mid)))
    if new_z <= z:
        left = mid+1
    else:
        right = mid-1

if int(((y+left)*100)/(x+left)) > z:
    print(left)
else:
    print(-1)