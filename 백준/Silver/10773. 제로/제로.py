import sys
N = int(sys.stdin.readline().rstrip())

result = []
for _ in range(N):
    tmp = int(sys.stdin.readline().rstrip())

    if tmp == 0:
        result.pop()
    else:
        result.append(tmp)

print(sum(result))