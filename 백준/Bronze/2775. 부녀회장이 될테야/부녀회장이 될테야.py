import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    N = int(sys.stdin.readline().rstrip())

    floor = [i for i in range(1, N+1)]

    for k in range(K):
        for n in range(1, N+1):
            if n == 1:
                floor[n-1] = 1
            else:
                floor[n-1] += floor[n-2]
    print(floor[-1])