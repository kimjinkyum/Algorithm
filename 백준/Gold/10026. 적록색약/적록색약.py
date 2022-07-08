import sys
sys.setrecursionlimit(1000000)

n = int(input())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    visited[x][y] = True

    current_color = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if not visited[nx][ny]:
            # print(x, y, nx, ny)
            if graph[nx][ny] == current_color:
                dfs(nx, ny)


result_not = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result_not += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

visited = [[False] * n for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            result += 1

print(result_not, result)
