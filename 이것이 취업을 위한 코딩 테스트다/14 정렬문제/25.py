# 실패율

N=3
stages=[1, 1, 1]


def solution(N, stages):
    answer = []
    stages.sort()
    fail_rate = {i: 0 for i in range(1, N + 2)}
    for s in stages:
        fail_rate[s] += 1

    for i in range(1, N + 1):
        tmp_sum = sum(fail_rate[s] for s in range(i, N + 1))
        if tmp_sum == 0:
            fail_rate[i] = 0
        else:
            fail_rate[i] = fail_rate[i] / tmp_sum
    fail_rate = sorted(fail_rate.items(), key=lambda item: (-(item[1]), item[0]))

    for a in fail_rate:
        if a[0] > N:
            continue
        answer.append(a[0])
    return answer


print(solution(N, stages))
