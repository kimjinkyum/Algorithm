# 정렬된 배열에서 특정 수의 개수 구하기
import sys
from bisect import bisect_left, bisect_right


def count_by_value(data, x):
    n = len(data)

    a = first(data, x, 0, n - 1)

    if a is None:
        return 0
    b = last(data, x, 0, n - 1)

    return b - a + 1


def first(data, target, s, e):
    if s > e:
        return None
    mid = (s + e) // 2

    if (mid == 0 or target > data[mid - 1]) and data[mid] == target:
        return mid

    elif data[mid] >= target:
        return first(data, target, s, mid - 1)

    else:
        return first(data, target, mid + 1, e)


def last(data, target, s, e):
    if s > e:
        return None
    mid = (s + e) // 2
    if (mid == len(data) - 1 or target < data[mid + 1]) and data[mid] == target:
        return mid
    elif data[mid] > target:
        return last(data, target, s, mid - 1)
    else:
        return last(data, target, mid + 1, e)


n, x = map(int, input().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

left = bisect_left(data, x)
right = bisect_right(data, x)

if left == right:
    print(-1)
else:
    print(right - left)

print(count_by_value(data, x))