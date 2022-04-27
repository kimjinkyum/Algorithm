# 카드 정렬하기
import sys
import heapq

N = int(input())

data = []

for _ in range(N):
    heapq.heappush(data, int(sys.stdin.readline().rstrip()))

result = 0

while len(data) != 1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)

    sum_result = a + b
    result += sum_result
    heapq.heappush(data, sum_result)

print(result)