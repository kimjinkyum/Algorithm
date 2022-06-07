import sys

n = int(input())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

result = 0
for i in range(n):
    for j in range(0, i+1):
        result += data[j]

print(result)