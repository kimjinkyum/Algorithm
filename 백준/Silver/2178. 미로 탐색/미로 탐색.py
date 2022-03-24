import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

maze = []

for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))


def BFS(graph, N, M):
    queue = deque()
    queue.append((0, 0))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        r, c = queue.popleft()
        for i in range(len(dx)):
            nr = r + dx[i]
            nc = c + dy[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if graph[nr][nc] == 0:
                continue
            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr, nc))
    return graph[N-1][M-1]

print(BFS(maze, N, M))

