N = input()
result = 0
for i in range(1,len(N)):
    result += i * (9 * pow(10,i-1))
result += len(N) * (int(N) - pow(10,len(N)-1) + 1)
print(result)

