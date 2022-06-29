from collections import deque


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(dist[x])
            break
        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                # print(i, dist[i])
                q.append(i)


dist = [0] * (100000 + 1)

n, k = map(int, input().split())

bfs()
