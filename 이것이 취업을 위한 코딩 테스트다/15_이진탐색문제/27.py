# 정렬된 배열에서 특정 수의 개수 구하기
import sys
from bisect import bisect_left, bisect_right
n, x = map(int, input().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

left = bisect_left(data, x)
right = bisect_right(data, x)

if left == right:
    print(-1)
else:
    print(right-left)


