# 안테나

n = int(input())

data = list(map(int, input().split()))

data.sort()

if len(data) % 2 == 0:
    print(data[len(data) // 2 - 1])
else:
    print(data[len(data) // 2])
