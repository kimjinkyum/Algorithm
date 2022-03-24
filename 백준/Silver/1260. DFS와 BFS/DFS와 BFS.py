from collections import deque
import sys

N, M, root = sys.stdin.readline().rstrip().split(" ")

graph_list = [[] for _ in range(int(N)+1)]
visited = [False] * (int(N)+1)

for _ in range(int(M)):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split(" "))
    graph_list[v1].append(v2)
    graph_list[v2].append(v1)

for i in range(1, int(N)+1):
    graph_list[i].sort()

def BFS(graph, root, visited):
    queue = deque([root])
    visited[root] = True
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for v in graph[n]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


def DFS(graph, root, visited):
    visited[root] = True

    print(root, end=" ")

    for i in graph[root]:
        if not visited[i]:
            DFS(graph, i, visited)


result_DFS = (DFS(graph_list, int(root), visited))
print()
visited = [False for i in range(int(N)+1)]
result_BFS = (BFS(graph_list, int(root), visited))

