# 볼링공 고르기

import sys
from itertools import combinations

n, m = map(int, (input().split(" ")))
data = list(map(int, sys.stdin.readline().rstrip().split(" ")))

arr = [0] * 11

for x in data:
    arr[x] += 1

result = 0

for i in range(1, m+1):
    n -= arr[i]
    result += arr[i] * n

print(result)


# 내 풀이
combi = list(combinations([i for i in range(n)], 2))

result = len(combi)
for x, y in combi:
    if data[x] == data[y]:
        result -= 1

print(result)
