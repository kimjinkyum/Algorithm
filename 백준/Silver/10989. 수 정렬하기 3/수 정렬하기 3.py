import sys

N = int(sys.stdin.readline().rstrip())

result = [0 for _ in range(10000)]
for i in range(N):
    result[int(sys.stdin.readline().rstrip())-1] += 1


for i in range(len(result)):
    if result[i] == 0:
        continue;
    else:
        for _ in range(result[i]):
            print(i + 1)

