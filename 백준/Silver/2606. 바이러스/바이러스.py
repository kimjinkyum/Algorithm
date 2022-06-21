import sys
from collections import deque
n = int(input())
m = int(input())

graph = [[] * (n+1) for _ in range(n+1)]

vistied = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    graph[a].append(b)
    graph[b].append(a)


vistied[1] = True
q = deque([1])
result = 0

while q:
    now = q.popleft()

    for i in graph[now]:
        if not vistied[i]:
            q.append(i)
            vistied[i] = True
            result += 1

print(result)