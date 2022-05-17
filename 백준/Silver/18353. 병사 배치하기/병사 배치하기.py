# 병사 배치하기
import sys

n = int(input())

data = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * n
data.reverse()


for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[j] + 1, dp[i])

result = n - max(dp)

print(result)

