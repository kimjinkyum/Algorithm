# 기둥과 보 설치

import sys

n = 5

build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]


def check(answer):
    for data in answer:
        x, y, a = data
        if a == 0:
            if [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer or y == 0:
                continue
            return False

        if a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue

            return False
    return True


def solution(n, build_frame):
    answer = []
    # board = [[-1] * (n + 1) for i in range(n + 1)]

    for frame in build_frame:
        x, y, a, b = frame
        if b == 0:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])

    return sorted(answer)


print(solution(n, build_frame))
