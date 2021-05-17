import sys

def recursive(temp, index, add, sub, mul, div):
    global max_num, min_num
    if index == n:
        max_num, min_num = max(max_num, temp), min(min_num, temp)
        return

    if add: recursive(temp+nums[index],index+1,add-1,sub,mul,div)
    if sub: recursive(temp-nums[index],index+1,add,sub-1,mul,div)
    if mul: recursive(temp*nums[index],index+1,add,sub,mul-1,div)
    # '//' 연산자를 사용하게 되면 음수연산때 원하는 값을 얻기 힘들다.
    if div: recursive(int(temp/nums[index]),index+1,add,sub,mul,div-1)

# 입력
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())
max_num, min_num = float('-inf'), float('inf')

recursive(nums[0], 1, add, sub, mul, div)
print(max_num,min_num,sep='\n')
