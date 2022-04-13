# 볼링공 고르기

import sys
from itertools import combinations

n, m = map(int, (input().split(" ")))

data = list(map(int, sys.stdin.readline().rstrip().split(" ")))

combi = list(combinations([i for i in range(n)], 2))

result = len(combi)
for x, y in combi:
    if data[x] == data[y]:
        result -=1

print(result)