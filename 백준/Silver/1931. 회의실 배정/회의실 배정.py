import sys

data = []

n = int(input())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    data.append((x, y))

data.sort(reverse=True)

index = 1
start_time = data[0][0]
result = 1
while True:
    if index >=n:
        break
    if data[index][1] > start_time:
        index += 1
    else:
        start_time = data[index][0]
        result += 1
        index += 1
        
print(result)