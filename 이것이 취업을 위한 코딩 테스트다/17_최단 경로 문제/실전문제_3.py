import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, y = map(int, input().split())
    graph[a].append((b, y))

def dijk(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijk(c)
max_time = 0
result = 0

for di in distance:
    if di == INF:
        continue
    result += 1
    if max_time < di:
        max_time = di

print(result-1, max_time)