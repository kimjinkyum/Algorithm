import sys

m, n = map(int, input().split())

graph = []
xs = []
ys = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(m):
        if tmp[j] == 1:
            xs.append(i)
            ys.append(j)
    graph.append(tmp)


def dfs(x, y, graph):
    if x < 0 or x >= n or y < 0 or y >= m:
        return graph
    new_x = []
    new_y = []
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if graph[next_x][next_y] == 0 and graph[x][y] == 1:
            graph[next_x][next_y] = 1
            new_y.append(next_y)
            new_x.append(next_x)

    return graph, new_x, new_y




result = 0
while True:
    new_xs = []
    new_ys = []
    for i in range(len(xs)):
        graph, tmp_x, tmp_y = dfs(xs[i], ys[i], graph)
        if tmp_x:
            new_xs.extend(tmp_x)
            new_ys.extend(tmp_y)
    xs = new_xs
    ys = new_ys
    if not xs:
        break
    result += 1

flag = True
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = False
            break

if flag:
    print(result)
else:
    print(-1)