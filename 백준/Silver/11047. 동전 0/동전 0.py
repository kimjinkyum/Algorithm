import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline().rstrip()))

count = 0

coin.sort(reverse=True)
for c in coin:
    count += (K//c)
    K = K % c

    if K == 0:
        break
print(count)

