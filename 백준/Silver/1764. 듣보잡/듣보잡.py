import sys
from collections import defaultdict

n, m = map(int, input().split())

data = defaultdict(set)


for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    data[tmp].add("HEAR")

for _ in range(m):
    tmp = sys.stdin.readline().rstrip()
    data[tmp].add("SEE")

result = 0
answer = []
for i in data.keys():
    if len(data[i]) > 1:
        result += 1
        answer.append(i)

print(result)
answer.sort()
for i in answer:
    print(i)