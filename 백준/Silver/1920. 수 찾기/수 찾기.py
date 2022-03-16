import sys
import bisect

N = int(sys.stdin.readline().rstrip())

num = (sys.stdin.readline().rstrip().split(" "))
num = list(map(int, num))
num = sorted(num)


M = int(sys.stdin.readline().rstrip())
find = (sys.stdin.readline().rstrip().split(" "))
find = list(map(int, find))

for f in find:
    l = bisect.bisect_left(num, f)
    r = bisect.bisect_right(num, f)

    if l == r:
        print(0)
    else:
        print(1)
