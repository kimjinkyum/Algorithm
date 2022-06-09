import sys
import heapq

n = int(input())
max_heap = []
for _ in range(n):
    value = int(sys.stdin.readline())

    if value == 0:
        if max_heap:
            print(- heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, - value)

