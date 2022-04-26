# 특정 거리의 도시 찾기
import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[0]].append(data[1])

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])


while queue:
    now = queue.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)

check = False
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)


