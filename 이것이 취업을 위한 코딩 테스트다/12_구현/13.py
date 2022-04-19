# 치킨 배달
import sys
from itertools import combinations


def find_distance(house, store):
    result = 0
    for h in house:
        result += min([abs(h[0] - store[i][0]) + abs(h[1] - store[i][1]) for i in range(len(store))])
    return result


n, m = map(int, input().split())
store = []
house = []
for r in range(n):
     data = (list(map(int, sys.stdin.readline().rstrip().split())))
     for c in range(n):
         if data[c] == 1:
             house.append([r, c])
         if data[c] == 2:
            store.append([r, c])

if len(store) == m:
    print(find_distance(house, store))
else:
    result_list = []
    for c in combinations(store, m):
        result_list.append(find_distance(house, c))
    print(min(result_list))
