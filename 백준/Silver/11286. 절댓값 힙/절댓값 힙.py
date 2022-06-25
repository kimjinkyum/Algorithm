import sys
import heapq

n = int(input())
data = []
for _ in range(n):
    value = int(sys.stdin.readline().rstrip())

    if value == 0:
        if data:
            print(heapq.heappop(data)[1])
        else:
            print(0)


    else:
        heapq.heappush(data,(abs(value), value))

