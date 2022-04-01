# 모함가 길드

import sys

n = int(input())
data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()
result = 0
count = 0
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
