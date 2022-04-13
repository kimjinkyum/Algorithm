# 만들 수 없는 금액

import sys

n = int(input())

coin = list(map(int, sys.stdin.readline().rstrip().split(" ")))

coin.sort()

target = 1

for x in coin:
    if target < x:
        break
    target += x

print(target)