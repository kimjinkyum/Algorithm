import sys

data = []

N = int(input())

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))

    data.append(tmp)

answer = [0, 0]


def solution(x, y, N):
    color = data[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != data[i][j]:
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return
    answer[color] += 1


solution(0, 0, N)
print(answer[0])
print(answer[1])
