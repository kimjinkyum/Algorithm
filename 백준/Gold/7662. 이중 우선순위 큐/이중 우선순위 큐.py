import sys
import heapq

t = int(input())

for _ in range(t):
    max_heap, min_heap = [], []
    k = int(sys.stdin.readline().rstrip())

    valid = [False] * 1000001
    for key in range(k):
        cmd = sys.stdin.readline().rstrip().split()
        if cmd[0] == "I":
            value = cmd[1]
            heapq.heappush(min_heap, (int(value), key))
            heapq.heappush(max_heap, (- int(value), key))
            valid[key] = True
        if cmd[0] == "D":
            if cmd[1] == "-1":
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    value = heapq.heappop(min_heap)
                    valid[value[1]] = False
            elif cmd[1] == "1":
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    value = heapq.heappop(max_heap)
                    valid[value[1]] = False

    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
