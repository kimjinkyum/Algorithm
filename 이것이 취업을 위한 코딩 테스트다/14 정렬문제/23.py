# 국영수
import sys

n = int(input())
data = []
for _ in range(n):
    tmp = sys.stdin.readline().rstrip().split()
    data.append(tmp)


data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for d in data:
    print(d[0])
