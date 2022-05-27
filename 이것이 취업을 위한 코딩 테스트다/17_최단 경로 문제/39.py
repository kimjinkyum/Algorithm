import sys
import heapq

def finding():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(len(dx)):
            curr_x = x + dx[i]
            curr_y = y + dy[i]
            if curr_x < 0 or curr_y < 0 or curr_x >= n or curr_y >= n:
                continue
            cost = dist + graph[curr_x][curr_y]
            if cost < distance[curr_x][curr_y]:
                distance[curr_x][curr_y] = cost
                heapq.heappush(q, (cost, curr_x, curr_y))

    return (distance[n-1][n-1])

INF = int(1e9)

t = int(input())
result = []

for _ in range(t):

    n = int(input())

    distance = [[INF] * (n) for _ in range(n)]
    graph = []

    for i in range(n):
        tmp= list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append(tmp)

    result.append(finding())
print(result)


