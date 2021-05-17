import sys

input = sys.stdin.readline
N = int(input())
city = list(map(int, input().split()))
station = list(map(int, input().split()))

min_price = float('inf')
result = 0
for distance, price in zip(city, station):
    if min_price > price:
        min_price = price
    result += distance * min_price

print(result)





