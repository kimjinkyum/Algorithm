import sys
from collections import defaultdict

n, m = map(int, input().split())

data = defaultdict()
data2 = defaultdict()

for i in range(1, n+1):
    tmp = sys.stdin.readline().rstrip()
    data[i] =tmp
    data2[tmp] = i

for _ in range(m):
    cmd = sys.stdin.readline().rstrip()

    if cmd.isnumeric():
        print(data[int(cmd)])
    else:
        print(data2[cmd])
