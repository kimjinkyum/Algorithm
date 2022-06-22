import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().rstrip().split())

data = defaultdict()

for _ in range(N):
    site, pw = sys.stdin.readline().rstrip().split()
    data[site] = pw

for _ in range(M):
    si = sys.stdin.readline().rstrip()

    print(data[si])