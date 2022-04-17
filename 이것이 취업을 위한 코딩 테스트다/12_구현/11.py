# 뱀

import sys

n = int(input())
k = int(input())

board = [[0] * (n + 1) for _ in range(n + 1)]
apple = []
dir = []

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))

    board[a][b] = 1

l = int(input())

for _ in range(l):
    dir.append(sys.stdin.readline().rstrip().split(" "))

time = 0
time_index = 0


def turn(direct, prev):
    if direct == "L":
        return (prev - 1) % 4
    else:
        return (prev + 1) % 4


direction = 0
x, y = 1, 1
board[x][y] = 2
q = [(x, y)]

while True:

    nx = x + dx[direction]
    ny = y + dy[direction]

    if n >= nx >= 1 and n >= ny >= 1 and board[nx][ny] != 2:
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            q.append((nx, ny))
            px, py = q.pop(0)
            board[px][py] = 0
        if board[nx][ny] == 1:
            board[nx][ny] = 2
            board[nx][ny] = 0
            q.append((nx, ny))
    else:
        time += 1
        break
    x, y = nx, ny
    time += 1

    if time_index < l and time == int(dir[time_index][0]):
        direction = turn(dir[time_index][1], direction)
        time_index += 1



print(time)
