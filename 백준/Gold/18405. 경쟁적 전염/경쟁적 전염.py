# 경쟁적 전염
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
graph = []

cord = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(N):
        if tmp[j]!=0:
            cord.append((tmp[j], i, j))
    graph.append((tmp))


S, X, Y = map(int, sys.stdin.readline().rstrip().split())

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_cord = []
    while q:
        x, y = q.pop()
        for i in range(len(dx)):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_y <0 or new_x >=N or new_y>=N:
                continue
            if graph[new_x][new_y] == 0:
                graph[new_x][new_y] = graph[x][y]
                new_cord.append((graph[x][y], new_x, new_y))

    return new_cord

cord.sort()

for _ in range(S):
    new_cord = []
    for c in range(len(cord)):
        _, x, y = cord[c]
        tmp = bfs(x, y)
        new_cord.extend(tmp)
    cord = new_cord
    cord.sort()

print(graph[X-1][Y-1])