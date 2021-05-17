import sys

input = sys.stdin.readline

number = 1
while True:
    l,p,v = map(int, input().split())
    if l+p+v == 0:
        break
    else:
        result = (v//p)*l + min(v%p, l)
        print("Case %d: %d" %(number,result))
        number += 1
