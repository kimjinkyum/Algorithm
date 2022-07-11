import sys

n = int(input())

data = list(map(int, sys.stdin.readline().rstrip().split()))
result = []

for i, v in enumerate(data):
    result.append((v, i))
result.sort()

answer = [(result[0][1], 0)]
indexs = 0

for i in range(1, n):
    if result[i - 1][0] != result[i][0]:
        indexs += 1
    answer.append((result[i][1], indexs))

answer.sort()

for a in answer:
    print(a[1],end=" ")

