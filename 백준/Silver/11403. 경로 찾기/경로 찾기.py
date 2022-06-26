import sys

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if data[a][k] != 0 and data[k][b] != 0:
                data[a][b] = 1

for a in range(n):
    for b in range(n):
        print(data[a][b], end=" ")
    print("")