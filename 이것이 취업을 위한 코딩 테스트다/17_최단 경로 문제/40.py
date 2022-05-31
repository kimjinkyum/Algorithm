import sys
import heapq
n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


q = []

heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

max_value = max(distance[1:])
max_index = 0
result = 0
for i in range(1, len(distance)):
    if distance[i] == max_value:
        if result == 0:
            max_index = i
        result += 1

print(max_index, max_value, result)