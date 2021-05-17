x = int(input())
nums = [0] * (x+1)
for i in range(2,len(nums)):
    if i%5 == 0:
        nums[i] = min(nums[i//5] + 1, nums[i-1] + 1)
        print(i, nums[i])
    elif i%3 == 0:
        nums[i] = min(nums[i//3] + 1, nums[i-1] + 1)
        print(i, nums[i])
    elif i%2 == 0:
        nums[i] = min(nums[i//2] + 1, nums[i-1] + 1)
        print(i, nums[i])
    else:
        nums[i] = nums[i-1] + 1
        print(i, nums[i])
print(nums[x])