from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스, 시간, 위치
            data.append(graph[i][j], 0, i, j)

data.sort()
q = deque(data)

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    v, s, x, y = q.popleft()

    if s == S:
        break
    for i in range(4):
        nx = x + dx[0]
        ny = y + dy[0]

        if 0 < nx or 0 < ny or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append(v, s + 1, nx, ny)

print(graph[X - 1][Y - 1])
