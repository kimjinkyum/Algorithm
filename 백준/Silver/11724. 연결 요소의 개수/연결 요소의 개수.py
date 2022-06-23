import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * i for i in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(s):
    q = deque([s])
    while q:
        n = q.pop()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


result = 0

for i in range(1, N + 1):
    if not visited[i]:
        result += 1
        bfs(i)

print(result)
