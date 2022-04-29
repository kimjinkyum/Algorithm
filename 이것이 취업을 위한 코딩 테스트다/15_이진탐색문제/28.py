# 고정점 찾기
import sys

n = int(input())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

start = 0
end = n

while True:
    if start >= end:
        print(-1)
        break
    mid = (start + end) // 2
    if data[mid] == mid:
        print(data[mid])
        break
    elif data[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
