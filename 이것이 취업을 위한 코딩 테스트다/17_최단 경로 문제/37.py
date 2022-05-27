# 플로이드
import sys

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    graph[a][b] = min(graph[a][b], c)

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

# 플로이드 워셜

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(-1, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
