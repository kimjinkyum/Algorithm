# 문자열 재정렬

import sys

data = sys.stdin.readline().rstrip()
result_sum = 0

result = []

for d in data:
    if d.isdigit():
        result_sum += int(d)
    else:
        result.append(d)

result.sort()
for i in result:
    print(i, end="")

print(result_sum)
