# 정수 삼각형

import sys

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))


for i in range(1, n):
    for j in range(i +1):
        if j == 0:
            up_left = 0
        else:
            up_left = data[i-1][j-1]

        if i == j:
            up = 0
        else:
            up = data[i-1][j]
        data[i][j] = data[i][j] + max(up_left, up)

print(max(data[n-1]))